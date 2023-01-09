from rest_framework.decorators import action
from rest_framework.response import Response
from . import services
from .serializers import FanSerializer


class LikedMixin:

    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        # Поставить лайк
        obj = self.get_object()
        services.add_like(obj, request.user)
        return Response()

    @action(detail=True, methods=['POST'])
    def unlike(self, request, pk=None):
        # Убрать поставленный лайк
        obj = self.get_object()
        services.remove_like(obj, request.user)
        return Response()

    @action(detail=True, methods=['GET'])
    def fans(self, request, pk=None):
        # Получить всех лайкнувших пользователей
        obj = self.get_object()
        fans = services.get_fans(obj)
        serializer = FanSerializer(fans, many=True)
        return Response(serializer.data)
