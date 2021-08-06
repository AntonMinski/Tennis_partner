from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'profiles', views.UserProfileViewSet)
router.register(r'messages', views.MessageViewSet)

profile_list = views.UserProfileViewSet.as_view({'get': 'list'})
profile_detail = views.UserProfileViewSet.as_view({'get': 'retrieve'})





urlpatterns = [
    # path('profiles/', views.UserProfileList.as_view(), name='user-profile-list')

    # path('profiles/', profile_list, name='user-profile-list'),
    # path('profiles/<int:pk>/', profile_detail, name='user-profile-detail'),

    path("", include(router.urls)),
    path('avatar/', views.AvatarUpdateView.as_view(), name='avatar-update'),

]
