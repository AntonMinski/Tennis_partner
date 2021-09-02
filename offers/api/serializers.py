from rest_framework import serializers
from offers.models import Offer, Message
from datetime import datetime


class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.StringRelatedField(source='sender')
    receiver_name = serializers.StringRelatedField(source='receiver')

    class Meta:
        model = Message
        exclude = ['updated_at']




class OfferSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    receiver_name = serializers.StringRelatedField(source='user.username',
                                                   read_only=True)
    class Meta:
        model = Offer
        fields = "__all__"
