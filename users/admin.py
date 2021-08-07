from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile, Message, BaseUser


class BaseUserAdmin(UserAdmin):
    model = BaseUser
    list_filter = ['username', 'email', 'is_staff']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'city']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'message_short_content']

    def message_short_content(self, obj):
        return f'{obj.message_content[:30]} ...'


admin.site.register(BaseUser, BaseUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Message, MessageAdmin)

