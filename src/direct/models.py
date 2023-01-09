from django.db import models
from django.conf import settings


class Dialog(models.Model):
    # Модель диалога (чат личных сообщений)
    auth_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='auth_user'
    )
    companion = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='companion'
    )

    def __str__(self):
        return f'Диалог {self.auth_user.username} с {self.companion.username}'

    class Meta:
        verbose_name = 'Диалог'
        verbose_name_plural = 'Диалоги'


class Message(models.Model):
    # Модель сообщения в диалоге
    dialog = models.ForeignKey(
        Dialog, 
        on_delete=models.CASCADE, 
        related_name='messages'
    )
    text = models.TextField(max_length=1000)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='messages'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Сообщение от {self.author.username}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-created_at']
