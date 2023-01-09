from django.contrib.contenttypes.models import ContentType
from ..account.models import CustomUser
from .models import Like


def add_like(obj, user):
    # Поставить лайк
    obj_type = ContentType.objects.get_for_model(obj)
    like = Like.objects.get_or_create(content_type=obj_type, object_id=obj.id, user=user)
    return like

def remove_like(obj, user):
    # Убрать поставленный лайк
    obj_type = ContentType.objects.get_for_model(obj)
    Like.objects.filter(content_type=obj_type, object_id=obj.id, user=user).delete()

def is_fan(obj, user) -> bool:
    # Проверка, поставлен ли лайк
    if not user.is_authenticated:
        return False
    obj_type = ContentType.objects.get_for_model(obj)
    likes = Like.objects.filter(content_type=obj_type, object_id=obj.id, user=user)
    return likes.exists()

def get_fans(obj):
    # Получение всех пользователей, который поставили лайк
    obj_type = ContentType.objects.get_for_model(obj)
    return CustomUser.objects.filter(likes__content_type=obj_type, likes__object_id=obj.id)
