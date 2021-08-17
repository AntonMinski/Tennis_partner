from rest_framework import serializers
from users.models import UserProfile, Message, BaseUser


class BaseUserSerializer(serializers.ModelSerializer):
    # id = serializers.StringRelatedField(read_only=True)
    # password = serializers.RelatedField(write_only=True)


    class Meta:
        model = BaseUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'username': {'write_only': True},
            'email': {'write_only': True},
            'first_name': {'write_only': True},
            'last_name': {'write_only': True},
            'password': {'write_only': True},
        }
        # write_only_fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        # fields = "__all__"


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


class MessageSerializer(serializers.ModelSerializer):

    sender = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Message
        fields = "__all__"