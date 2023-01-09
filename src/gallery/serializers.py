from rest_framework import serializers
from ..utils.serializers import RecursiveSerializer, FilterCommentListSerializer
from ..like import services as like_service
from .models import Publication, Comment


class CreateCommentSerializer(serializers.ModelSerializer):
    # Добавление комментария к публикации
    class Meta:
        model = Comment
        fields = (
            'publication', 
            'text', 
            'parent',
        )


class CommentSerializer(serializers.ModelSerializer):
    # Комментарий
    text = serializers.SerializerMethodField()
    children = RecursiveSerializer(many=True)
    user = serializers.ReadOnlyField(source='user.username')

    def get_text(self, obj):
        if obj.is_deleted:
            return None
        return obj.text

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = (
            'id', 
            'publication', 
            'user', 
            'text', 
            'created_at', 
            'updated_at', 
            'children',
        )


class PublicationListSerializer(serializers.ModelSerializer):
    # Список публикаций
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Publication
        fields = (
            'id', 
            'user', 
            'image', 
            'created_at', 
            'likes_count',
            'comments_count',
        )


class PublicationSerializer(serializers.ModelSerializer):
    # Публикация
    user = serializers.ReadOnlyField(source='user.username')
    is_fan = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Publication
        fields = (
            'id', 
            'user', 
            'image',
            'description',
            'created_at', 
            'is_fan',
            'likes_count',
            'comments',
        )

    def get_is_fan(self, obj) -> bool:
        # Проверка, лайкнул ли пользователь (request.user) публикацию (obj)
        user = self.context.get('request').user
        return like_service.is_fan(obj, user)
