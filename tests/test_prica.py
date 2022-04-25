import pytest
from django.urls import reverse
from django.test import Client

from prica.models import PricaModel
from tests.factories import PricaFactory, UserFactory


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
    PricaFactory(sender=user)
    PricaFactory(reciever=user, sender=admin_user)

    url = reverse("price")
    response = client.get(url)

    assert response.status_code == 200, "Expect 200 response since user is logged in"
    assert response.context.get("price").count() == 2, "Expect that both messages are return in query"


@pytest.mark.django_db
def test_send_message_to_admin(auth_client):
    client, user = auth_client
    admin_user = UserFactory(is_staff=True, is_superuser=True)
    url = reverse("home-prica")

    message = "testing text"

    response = client.post(url, {"text": message})

    assert response.status_code == 200
    assert PricaModel.objects.filter(sender=user, text=message, reciever=admin_user).exists()


@pytest.mark.django_db
def test_send_message_from_admin_to_user():
    admin_user = UserFactory(is_staff=True, is_superuser=True)
    client = Client()
    client.force_login(admin_user)
    user = UserFactory()
    message = "testing text"

    url = reverse("home-prica")

    response = client.post(url, {"reciever": user.id, "text": message})

    assert response.status_code == 200
    assert PricaModel.objects.filter(sender=admin_user, text=message, reciever=user).exists()
