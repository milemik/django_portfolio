import pytest
from django.test import Client
from django.urls import reverse

from tests.factories import UserFactory, PricaModelFactory


@pytest.mark.django_db
def test_get_num_of_unread_messages():
    user = UserFactory()
    client = Client()
    url = reverse("unread-messages", kwargs={"user_id": user.id})
    response = client.get(url)
    assert response.status_code == 200
    assert response.json().get("unread") == 0


@pytest.mark.django_db
def test_get_num_of_unread_messages_has_unread():
    unread_num = 3
    user = UserFactory()
    PricaModelFactory.create_batch(unread_num, reciever=user)
    PricaModelFactory(sender=user)  # this one shouldn't be counted as unread, since user is sender
    client = Client()
    url = reverse("unread-messages", kwargs={"user_id": user.id})
    response = client.get(url)
    assert response.status_code == 200
    assert response.json().get("unread") == unread_num
