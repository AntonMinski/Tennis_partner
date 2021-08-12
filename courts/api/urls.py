from django.urls import path
from . import views

urlpatterns = [
    path("", views.CourtListCreateApiView.as_view(), name="court_list"),
    path("<int:pk>/", views.CourtEditApiView.as_view(), name="court_detail"),
    path("<int:pk>/review/", views.ReviewCreateApiView.as_view(),
         name="court_review"),
    path("<int:pk>/", views.ReviewEditApiView.as_view(),
         name="review_detail"),

]


