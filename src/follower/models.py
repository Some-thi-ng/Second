from django.conf import settings
from django.db import models


class Follower(models.Model):
    # Модель подписчика
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner')
    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriber')

    def __str__(self):
        return f'{self.subscriber.username} подписан на {self.user.username}'

    class Meta:
        verbose_name = 'Подписчики'
        verbose_name_plural = verbose_name
