from django.urls import path

from . import views

urlpatterns = [
    path("singup/", views.maintenance, name="singup"),
    path("login/", views.maintenance, name="login"),
    path("logout/", views.maintenance, name="logout"),
    path("profile/", views.maintenance, name="profile"),
]
