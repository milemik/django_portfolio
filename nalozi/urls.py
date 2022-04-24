from django.urls import path

from . import views

urlpatterns = [
    path("singup/", views.singup, name="singup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("delete/", views.delete_user, name="delete-user")
]
