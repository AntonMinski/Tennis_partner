from rest_framework import generics, mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

# from users.api.permissions import IsOwnerOrReadOnly, IsOwnProfileOrReadOnly
from users.api.serializers import UserProfileSerializer, \
    UserProfileAvatarSerializer, MessageSerializer

from users.models import UserProfile, Message


class UserProfileList(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]