from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


offers_router = DefaultRouter()
offers_router.register(r'', views.OfferViewSet)

offer_list = views.OfferViewSet.as_view({'get': 'list'})
offer_detail = views.OfferViewSet.as_view({'get': 'retrieve'})

message_router = DefaultRouter()
message_router.register(r'', views.MessageViewSet)
message_list = views.MessageViewSet.as_view({'get': 'list'})
message_detail = views.MessageViewSet.as_view({'get': 'retrieve'})



urlpatterns = [
    path("offers/", include(offers_router.urls)),
    path("messages/", include(message_router.urls)),
    path("messages_sent/", views.MessagesSentListAPIView.as_view()),
    path("messages_received/", views.MessagesReceivedListAPIView.as_view()),
]
