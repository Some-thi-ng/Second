from rest_framework import serializers
from ..account.serializers import CustomUserByListSerializer
from .models import Dialog, Message


class CreateMessageSerializer(serializers.ModelSerializer):
    # Добавление сообщения в диалоге
    class Meta:
        model = Message
        fields = (
            'dialog',
            'text'
        )


class MessageSerializer(serializers.ModelSerializer):
    # Информация о выводимых сообщениях в диалоге
    author = CustomUserByListSerializer()
    class Meta:
        model = Message
        fields = (
            'id',
            'author',
            'text',
            'created_at',
            'dialog',
        )


class DialogSerializer(serializers.ModelSerializer):
    # Информация о диалоге
    auth_user = CustomUserByListSerializer(read_only=True)
    companion = CustomUserByListSerializer(read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Dialog
        fields = (
            'id', 
            'auth_user', 
            'companion', 
            'messages', 
        )


class DialogListSerializer(serializers.ModelSerializer):
    # Список диалогов
    last_message = serializers.SerializerMethodField()
    class Meta:
        model = Dialog
        fields = (
            'auth_user',
            'companion',
            'last_message',
        )

    def get_last_message(self, obj: Dialog):
        # Вывод последнего сообщения
        return MessageSerializer(obj.messages.order_by('created_at').last()).data
