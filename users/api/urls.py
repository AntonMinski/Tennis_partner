from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.UserProfileList.as_view(), name='user-profile-list')
]
