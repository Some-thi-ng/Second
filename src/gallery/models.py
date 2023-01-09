from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.contrib.contenttypes.fields import GenericRelation
from ..like.models import Like
from ..utils.tools import get_path_upload_image
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Publication(models.Model):
    # Модель публикации
    image = models.FileField(
        'Публикация', 
        upload_to=get_path_upload_image,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'mov', 'mp4'])],
    )
    description = models.CharField('Описание', max_length=2000, blank=True, null=True)
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)
    updated_at = models.DateTimeField('Изменено', auto_now=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='images')
    like = GenericRelation(Like)

    def __str__(self):
        return f'{self.id} от {self.user}'

    @property
    def likes_count(self):
        return self.like.count()

    def comments_count(self):
        return self.comments.count()

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-created_at']


class Comment(MPTTModel):
    # Модель комментария к публикации
    text = models.TextField('Текст', max_length=500)
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)
    updated_at = models.DateTimeField('Изменено', auto_now=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    is_deleted = models.BooleanField('Удалено', default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, related_name='comments', on_delete=models.CASCADE)
    parent = TreeForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return '{} - {}'.format(self.user, self.publication)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']
