from rest_framework import generics, mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, \
    BasicAuthentication, TokenAuthentication

# from users.api.permissions import IsOwnerOrReadOnly, IsOwnProfileOrReadOnly
from .serializers import UserProfileSerializer, \
    UserProfileAvatarSerializer, MessageSerializer, BaseUserSerializer
from .permissions import IsOwnPofileOrRead_only, IsOwnerOrReadOnly

from users.models import UserProfile, Message, BaseUser
from users.forms import CustomUserForm


class BaseUserViewSet(generics.ListAPIView):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer
    permission_classes = [IsAdminUser]





class RegisterCreateApiView(generics.ListCreateAPIView):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer
    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]


class UserProfileViewSet_old(mixins.UpdateModelMixin, mixins.ListModelMixin,
                         mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnPofileOrRead_only]


class UserProfileListApiView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnPofileOrRead_only]



    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnPofileOrRead_only]


class MessageViewSet(ModelViewSet):
    # queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['sender']

    '''
    # own
    def get_queryset(self):
        queryset = Message.objects.all()
        username = self.request.user.userprofile  # get username or make it None
        # print(self.request.user.userprofile)
        if not username:
            username = None
        queryset = queryset.filter(sender__user__username=username)  # username same as parametr
        return queryset
    '''

    #  tutorial
    def get_queryset(self):
        queryset = Message.objects.all()
        username = self.request.query_params.get("username", None)  # get username from "?username=" from url
        if username:
            queryset = queryset.filter(sender__user__username=username)
        return queryset

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