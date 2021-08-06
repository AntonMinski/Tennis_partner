from rest_framework import serializers
from users.models import UserProfile, Message


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