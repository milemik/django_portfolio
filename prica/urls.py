from django.urls import path
from .views import MyView, SveView

urlpatterns = [
    path("", MyView.as_view(), name="home-prica"),
    path("price/", SveView.as_view(), name="price"),
]
