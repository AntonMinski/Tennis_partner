# from rest_framework import generics, mixins, viewsets
# from rest_framework.filters import SearchFilter
# from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, viewsets, permissions, generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated


from .serializers import OfferSerializer, MessageSerializer
from offers.models import Offer, Message
from users.models import BaseUser
from .permissions import IsCreatorOrReadOnly


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all().order_by("-created_at", "-updated_at")
    serializer_class = OfferSerializer
    permission_classes = [IsCreatorOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # def get_queryset(self):
    #     # id = self.kwargs.get(id)
    #     return Offer.objects.all().order_by("-created_at")


class MessageListCreateAPIView(generics.ListCreateAPIView):
    """Allow users to answer a question instance if they haven't already."""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # receiver = get_object_or_404(BaseUser)
        serializer.save(sender=self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    """Allow users to answer a question instance if they haven't already."""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # receiver = get_object_or_404(BaseUser)
        serializer.save(sender=self.request.user)


