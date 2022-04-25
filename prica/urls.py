from django.urls import path
from .views import SendMessage, SveView

urlpatterns = [
    path("", SendMessage.as_view(), name="home-prica"),
    path("price/", SveView.as_view(), name="price"),
]
