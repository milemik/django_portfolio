from django.urls import path
from .views import SendMessage, SveView, MarkRead

urlpatterns = [
    path("", SendMessage.as_view(), name="home-prica"),
    path("price/", SveView.as_view(), name="price"),
    path("mark-read/", MarkRead.as_view(), name="mark-read-message"),
]
