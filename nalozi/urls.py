from django.urls import path

from . import views

urlpatterns = [
    path("singup/", views.maintenance, name="singup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.maintenance, name="profile"),
]
