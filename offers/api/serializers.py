from rest_framework import serializers
from offers.models import Offer, Message
from datetime import datetime


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField(read_only=True)
    # created_dt = serializers.SerializerMethodField()

    class Meta:
        model = Message
        exclude = ['updated_at']

    # def created_dt(self, instance):
    #     time = datetime.now()
    #     date_time = time.strftime("%m/%d/%Y, %H:%M:%S")
    #     return date_time


class OfferSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    receiver_name = serializers.StringRelatedField(source='user.username',
                                                   read_only=True)
    # created_at = serializers.SerializerMethodField()

    class Meta:
        model = Offer
        fields = "__all__"

    # def created_at(self, instance):
    #     time = datetime.now()
    #     date_time = time.strftime("%m/%d/%Y, %H:%M:%S")
    #     return time