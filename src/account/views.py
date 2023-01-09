from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, filters, parsers
from ..utils.tools import delete_old_file
from .models import CustomUser
from .serializers import (
    CustomUserSerializer, 
    CustomUserPublicSerializer, 
    CustomUserByListSerializer,
)


class CustomUserListView(ModelViewSet):
    # Список пользователей
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserByListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'display_name']


class CustomUserView(ModelViewSet):
    # Профиль авторизованного пользователя
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)

    def perform_destroy(self, instance):
        # Удаление старого avatar во время загрузки нового
        delete_old_file(instance.avatar.path)
        instance.delete()


class CustomUserPublicView(ModelViewSet):
    # Публичный профиль пользователя
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserPublicSerializer
    permission_classes = [permissions.AllowAny]
