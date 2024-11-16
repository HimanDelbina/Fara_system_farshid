from django.urls import path
from . import views

urlpatterns = [
    path("get_all_user", views.get_all_user),
]
