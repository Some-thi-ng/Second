from django.contrib import admin
from .models import Dialog, Message


@admin.register(Dialog)
class DialogAdmin(admin.ModelAdmin):
    # Диалоги
    list_display = ('id', 'auth_user', 'companion')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    # Сообщения в диалогах
    list_display = ('id', 'dialog', 'text', 'author', 'created_at')
    search_fields = ('dialog',)
    ordering = ('-created_at',)
