from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'', views.BaseUserViewSet)
router.register(r'messages', views.MessageViewSet, basename="status") # basename указывается в тестах (list_url = reverse("status-list")






urlpatterns = [
    path('profiles/', views.UserProfileListApiView.as_view(), name='user-profile-list'),
    path("", include(router.urls)),
    # path('avatar/', views.AvatarUpdateView.as_view(), name='avatar-update'),
    path('avatar/', views.AvatarUpdateView.as_view(), name='avatar-update'),

]
