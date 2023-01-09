from rest_framework import permissions, viewsets, response
from ..gallery.serializers import PublicationListSerializer
from .services import feed_service


class FeedView(viewsets.GenericViewSet):
    # Вывод ленты новостей
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PublicationListSerializer

    def list(self, request, *args, **kwargs):
        queryset = feed_service.get_post_list(request.user)
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)
