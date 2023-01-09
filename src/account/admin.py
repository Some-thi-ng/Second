from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'display_name', 'is_active')
    list_display_links = ('username', 'email')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'phone', 'password')}),
        (_('Personal info'), {'fields': ('display_name', 'gender', 'about', 'birthday', 'avatar')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active')}),
    )
    search_fields = ('username', 'display_name')
    ordering = ('-date_joined',)
