from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings


class BaseUser(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=35, blank=True)
    avatar = models.ImageField(null=True, blank=True)

    # def __str__(self):
    #     return self.user.username
    #
    # @property
    # def email(self):
    #     return self.user.email


class Message(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message_content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    # sender.email = models.ForeignKey(UserProfile.email)

    # def __str__(self):
    #     return str(self.user_profile)
