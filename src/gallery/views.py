from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, parsers
from ..like.mixins import LikedMixin
from ..utils.permissions import IsAuthor
from .serializers import PublicationListSerializer, PublicationSerializer, CreateCommentSerializer
from .models import Publication, Comment


class PublicationListView(ModelViewSet):
    # Вывод списка публикаций пользователя
    serializer_class = PublicationListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Publication.objects\
        .filter(user_id=self.kwargs.get('pk'))\
        .select_related('user')\
        .prefetch_related('comments')


class PublicationView(ModelViewSet, LikedMixin):
    # Вывод публикации
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = PublicationSerializer
    queryset = Publication.objects\
        .all()\
        .select_related('user')\
        .prefetch_related('comments')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes_by_action = {
        'get': [permissions.AllowAny],
        'update': [IsAuthor],
        'destroy': [IsAuthor]
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentView(ModelViewSet):
    # Вывод комментария к публикации
    queryset = Comment.objects.all()
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = CreateCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes_by_action = {
        'get': [permissions.AllowAny],
        'update': [IsAuthor],
        'destroy': [IsAuthor]
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
