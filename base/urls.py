from django.urls import path, re_path

from . import views

urlpatterns = [
        # re_path(r"^.*$", views.IndexTemplateView.as_view(), name='home'),
        path('', views.IndexTemplateView.as_view(), name='home'),
]

