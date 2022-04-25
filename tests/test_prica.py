import pytest
from django.urls import reverse
from django.test import Client

from prica.models import PricaModel
from tests.factories import PricaModelFactory, UserFactory


@pytest.mark.django_db
def test_sve_price_no_login_user():
    client = Client()
    url = reverse("price")

    response = client.get(url, follow=True)

    assert response.redirect_chain == [("/accounts/login/?next=/prica/price/", 302)], "Redirect to login"


@pytest.mark.django_db
def test_sve_price_no_messages(auth_client):
    client, _ = auth_client
    url = reverse("price")
    response = client.get(url)

    assert response.status_code == 200, "Expect 200 response since user is logged in"
    assert not response.context.get("prica"), "Expect that queryset is empty"


@pytest.mark.django_db
def test_sve_price_with_messages(auth_client):
    client, user = auth_client
    admin_user = UserFactory(is_staff=True)
    PricaModelFactory(sender=user)
    PricaModelFactory(reciever=user, sender=admin_user)

    url = reverse("price")
    response = client.get(url)

    assert response.status_code == 200, "Expect 200 response since user is logged in"
    assert response.context.get("price").count() == 2, "Expect that both messages are return in query"


@pytest.mark.django_db
def test_send_message_get(auth_client):
    client, user = auth_client
    url = reverse("home-prica")
    response = client.get(url)
    assert response.status_code == 200, "Expect that status code is 200"


@pytest.mark.django_db
def test_send_message_get_admin(admin_client):
    client, user = admin_client
    url = reverse("home-prica")
    response = client.get(url)

    assert response.status_code == 200, "Expect that status code is 200"


@pytest.mark.django_db
def test_send_message_to_admin(auth_client):
    client, user = auth_client
    admin_user = UserFactory(is_staff=True, is_superuser=True)
    url = reverse("home-prica")

    message = "testing text"

    response = client.post(url, {"text": message})

    assert response.status_code == 200, "Expect status code is 200"
    assert PricaModel.objects.filter(
        sender=user, text=message, reciever=admin_user
    ).exists(), "Expect that message is created"


@pytest.mark.django_db
def test_send_message_from_admin_to_user(admin_client):
    client, admin_user = admin_client
    user = UserFactory()
    message = "testing text"

    url = reverse("home-prica")

    response = client.post(url, {"reciever": user.id, "text": message})

    assert response.status_code == 200, "Check if response is OK"
    assert PricaModel.objects.filter(
        sender=admin_user, text=message, reciever=user
    ).exists(), "Expect that message is created with correct sender and reciver"


@pytest.mark.django_db
def test_mark_read_message(auth_client):
    client, auth = auth_client
    url = reverse("mark-read-message")
    message = PricaModelFactory()
    response = client.post(url, {"message_id": message.id}, follow=True)

    assert response.redirect_chain == [("/prica/price/", 302)], "Expect that we are redirected to all messages"
    message.refresh_from_db()
    assert message.is_read is True, "Expect that message is mark as read"
