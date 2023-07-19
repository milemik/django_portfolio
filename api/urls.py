from django.urls import path
from .views import get_num_of_unread_messages

urlpatterns = [path("num-unread/", get_num_of_unread_messages, name="unread-messages")]
