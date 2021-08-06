from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib.auth.models import User


class Court(models.Model):
    COVER_CHOICES = [
        ('CL', 'Clay'),
        ('HR', 'Hard'),
        ('GR', 'Grass'),
        ('CR', 'Carpet'),
    ]
    title = models.CharField(max_length=70)
    address = models.CharField(max_length=70)
    cover = models.CharField(choices=COVER_CHOICES, max_length=2)
    description = models.TextField()
    opening_date = models.DateField()

    def __str__(self):
        return self.title


class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review_author = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                         MaxValueValidator(5)])
    court = models.ForeignKey(Court, on_delete=models.CASCADE,
                              related_name='reviews')

    def __str__(self):
        return str(self.rating)


