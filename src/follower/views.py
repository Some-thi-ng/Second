from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import permissions, response
from .serializers import FollowerListSerializer
from ..account.models import CustomUser
from .models import Follower


class FollowerListView(ModelViewSet):
    # Вывод списка подписчиков пользователя
    serializer_class = FollowerListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Follower.objects.filter(user_id=self.kwargs.get('pk'))


class FollowerView(APIView):
    # Добавление/удаление подписчиков
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            user = CustomUser.objects.get(id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        Follower.objects.create(subscriber=request.user, user=user)
        print('Success')
        return response.Response(status=201)

    def delete(self, request, pk):
        try:
            sub = Follower.objects.get(subscriber=request.user, user_id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        sub.delete()
        print('Success')
        return response.Response(status=204)
