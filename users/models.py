from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
from django.contrib.postgres.fields import ArrayField, DecimalRangeField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core import validators


class BaseUser(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
    city = models.CharField(max_length=35, blank=True, null=True)
    avatar = models.ImageField(null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    sport_styles = ArrayField(models.CharField(max_length=20),
                              blank=True, null=True)
    age = models.IntegerField(null=True, validators=
                              [MinValueValidator(4), MaxValueValidator(130)])
    skill_level = ArrayField(models.FloatField(null=True, validators=
                              [MinValueValidator(1), MaxValueValidator(7)]),
                             null=True,
                             max_length=2)

