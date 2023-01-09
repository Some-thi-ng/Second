from rest_framework import serializers
from ..account.models import CustomUser



class FanSerializer(serializers.ModelSerializer):
    # Вывод лайкнувшего пользователя
    avatar = serializers.ImageField(read_only=True)
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'display_name',
            'avatar',
        )
