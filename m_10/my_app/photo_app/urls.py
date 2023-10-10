from django.urls import path, include

from . import views

app_name = "photo_app"

urlpatterns = [
    path("", views.index, name="main"),
]
