from rest_framework import generics, mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet

# from users.api.permissions import IsOwnerOrReadOnly, IsOwnProfileOrReadOnly
from .serializers import UserProfileSerializer, \
    UserProfileAvatarSerializer, MessageSerializer
from .permissions import IsOwnPofileOrRead_only, IsOwnerOrReadOnly

from users.models import UserProfile, Message

'''
class UserProfileList(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
'''

# same on viewsets:
class UserProfileViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin,
                         mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnPofileOrRead_only]


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        sender = self.request.user.userprofile
        serializer.save(sender=sender)


class AvatarUpdateView(generics.UpdateAPIView):
    # queryset = Message.objects.all()
    serializer_class = UserProfileAvatarSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.userprofile
        return profile_object