# from rest_framework import generics, mixins, viewsets
# from rest_framework.filters import SearchFilter
# from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, viewsets, permissions, generics, status
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


# взял тот же вариант ниже, этот пока не активен
class MessageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data_user_name = request.data['receiver']
        receiver = BaseUser.objects.get(username=data_user_name).id
        data = {
            'sender': request.user.id,
            'receiver': receiver,
            'content': request.data['content'],
        }
        serializer_context = {"request": request}
        serializer = self.serializer_class(data=data, context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessagesSentListAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        sent_messages = Message.objects.filter(
            sender=self.request.user).order_by('-created_at')
        return sent_messages


class MessagesReceivedListAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        received_messages = Message.objects.filter(
            receiver=self.request.user).order_by('-created_at')
        return received_messages

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        data_user_name = request.data['receiver']
        receiver = BaseUser.objects.get(username=data_user_name).id
        data = {
            'sender': request.user.id,
            'receiver': receiver,
            'content': request.data['content'],
        }
        serializer_context = {"request": request}
        serializer = self.serializer_class(data=data,
                                           context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
#     def perform_create(self, serializer):
#         print(self.kwargs)
#         serializer.save(sender=self.request.user, receiver='1', content='dfdffd')
