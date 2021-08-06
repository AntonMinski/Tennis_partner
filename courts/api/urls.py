from django.urls import path
from . import views

urlpatterns = [
    path("courts/", views.CourtListCreateApiView.as_view(), name="court_list"),
    path("courts/<int:pk>/", views.CourtEditApiView.as_view(), name="court_detail"),
    path("courts/<int:pk>/review/", views.ReviewCreateApiView.as_view(),
         name="court_review"),
    path("reviews/<int:pk>/", views.ReviewEditApiView.as_view(),
         name="review_detail"),

]


