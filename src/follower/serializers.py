from rest_framework import serializers
from ..account.serializers import CustomUserByListSerializer
from .models import Follower


class FollowerListSerializer(serializers.ModelSerializer):
    # Информация о подписчиках
    subscriber = CustomUserByListSerializer()
    class Meta:
        model = Follower
        fields = (
            'subscriber',
        )
