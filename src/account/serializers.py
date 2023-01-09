from rest_framework import serializers
from ..utils.tools import delete_old_file
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    # Сериализация информации об авторизованном пользователе
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'email',
            'phone',
            'avatar',
            'display_name',
            'subscriptions_count',
            'subscribers_count',
            'gender',
            'about',
            'birthday',
        )

    def update(self, instance, validated_data):
        delete_old_file(instance.avatar.path)
        return super().update(instance, validated_data)


class CustomUserPublicSerializer(serializers.ModelSerializer):
    # Сериализация публичной информации о пользователе
    avatar = serializers.ImageField(read_only=True)
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'avatar',
            'display_name',
            'subscriptions_count',
            'subscribers_count',
            'gender',
            'about',
            'birthday',
        )


class CustomUserByListSerializer(serializers.ModelSerializer):
    # Сериализация информация о пользователе в списках
    avatar = serializers.ImageField(read_only=True)
    class Meta:
        model = CustomUser
        fields = (
            'id', 
            'username', 
            'display_name', 
            'avatar',
        )
