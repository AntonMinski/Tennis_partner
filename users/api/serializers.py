from django.contrib.auth import authenticate
from rest_framework import serializers
from users.models import UserProfile, BaseUser


class LoginSerializer_old(serializers.Serializer):
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError(
                'Username is required to log in.'
            )
        if password is None:
            raise serializers.ValidationError(
                'Password is required to log in.'
            )

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
        return {
            'username': user.username,
            'token': user.token
        }


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseUser
        fields = ['username', 'password']
        extra_kwargs = {
            'username': {'write_only': True},
            'password': {'write_only': True},
        }


class BaseUserSerializer(serializers.ModelSerializer):
    # id = serializers.StringRelatedField(read_only=True)
    # password = serializers.RelatedField(write_only=True)

    class Meta:
        model = BaseUser
        fields = ['id', 'username', 'username', 'first_name', 'last_name', 'password']



class UserProfileSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserProfile
        fields = "__all__"


class UserProfileAvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ("avatar",)

