from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Publication, Comment


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    # Публикации
    list_display = ('id', 'user', 'is_published', 'created_at', 'likes_count')


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    # Комментарии к публикациям
    list_display = ('id', 'user', 'publication', 'created_at', 'updated_at', 'is_published')
    mptt_level_indent = 10
