from rest_framework import permissions, parsers, response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from ..account.models import CustomUser
from .serializers import CreateMessageSerializer, MessageSerializer, DialogListSerializer, DialogSerializer
from .models import Message, Dialog
from django.db.models import Q


class DialogListView(ModelViewSet):
    # Вывод списка диалогов пользователя
    serializer_class = DialogListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Dialog.objects.filter(Q(auth_user=self.request.user) | Q(companion=self.request.user))


class DialogView(ModelViewSet):
    # Вывод конкретного диалога
    serializer_class = DialogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Dialog.objects.filter(Q(auth_user=self.request.user) | Q(companion=self.request.user))

class CreateDialogView(APIView):
    # Создание диалога с определенным пользователем
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            user = CustomUser.objects.get(id=pk)
        except Dialog.DoesNotExist:
            return response.Response(status=404)
        Dialog.objects.create(auth_user=request.user, companion=user)
        print('Success')
        return response.Response(status=201)


class MessageView(ModelViewSet):
    # Вывод сообщений в диалоге
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = CreateMessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Message.objects.all().select_related('dialog')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
