from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.conf import settings
from .managers import CustomUserManager
from ..utils.tools import get_path_upload_avatar, validate_size_image


class CustomUser(AbstractUser):
    # Кастомная модель пользователя
    GENDER = {
        ('M', 'Мужской'),
        ('F', 'Женский'),
        ('N', 'Предпочитаю не указывать'),
    }

    username = models.CharField('Логин', max_length=50, unique=True)
    email = models.EmailField('Email', unique=True)
    display_name = models.CharField('Имя', max_length=50, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=14, unique=True, blank=True, null=True)
    gender = models.CharField('Пол', max_length=1, choices=GENDER, default='N')
    about = models.TextField('Обо мне', max_length=1000, blank=True, null=True)
    birthday = models.DateField('Дата рождения', blank=True, null=True)
    avatar = models.ImageField(
        'Аватар', 
        upload_to=get_path_upload_avatar, 
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_image],
        default=settings.DEFAULT_AVATAR,
        blank=True, 
        null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    # Количество подписок
    def subscriptions_count(self):
        return self.subscriber.count()

    # Количество подписчиков
    def subscribers_count(self):
        return self.owner.count()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-date_joined']
