from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile, BaseUser


class BaseUserAdmin(UserAdmin):
    model = BaseUser
    list_filter = ['username', 'username', 'is_staff']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'city']


admin.site.register(BaseUser, BaseUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)


