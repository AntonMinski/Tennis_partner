from rest_framework import generics, mixins, viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, \
    BasicAuthentication, TokenAuthentication
from django.contrib.auth.hashers import make_password
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication, JWTAuthentication

# from users.api.permissions import IsOwnerOrReadOnly, IsOwnProfileOrReadOnly
from .serializers import UserProfileSerializer, LoginSerializer, \
    UserProfileAvatarSerializer, MessageSerializer, BaseUserSerializer
from .permissions import IsOwnPofileOrRead_only, IsOwnerOrReadOnly

from users.models import UserProfile, Message, BaseUser
from users.forms import CustomUserForm


class BaseUserViewSet(generics.ListAPIView):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer
    permission_classes = [IsAdminUser]

import json

class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        user.set_password(request.data['password'])
        if user is not None:
            login(request, user)
            current_user = request.user
            data = {
                'result': 'sucess',
                'username': username,
                'userId': user.id,
                'password': password,
            }
            return Response(data, status=status.HTTP_200_OK)


class UserCreate(CreateAPIView):
    serializer_class = BaseUserSerializer

    def post(self, request, format='json'):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                user.set_password(request.data['password'])
                token = Token.objects.create(user=user)
                data = {
                    'result': 'user registered',
                    'token': token.key,
                }
                return Response(data, status=status.HTTP_201_CREATED)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet_old(mixins.UpdateModelMixin, mixins.ListModelMixin,
                         mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnPofileOrRead_only]


class UserProfileListApiView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnPofileOrRead_only]


class MessageViewSet(ModelViewSet):
    # queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsOwnPofileOrRead_only or IsAdminUser]

    def get_object(self):
        profile_object = self.request.user.userprofile
        return profile_object