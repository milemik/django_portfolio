import pytest
from django.urls import reverse
from django.test import Client

from tests.factories import PricaFactory, UserFactory


@pytest.mark.django_db
def test_sve_price_no_login_user():
    client = Client()
    url = reverse("price")

    response = client.get(url, follow=True)

    assert response.redirect_chain == [('/accounts/login/?next=/prica/price/', 302)]


@pytest.mark.django_db
def test_sve_price_no_messages(auth_client):
    client, _ = auth_client
    url = reverse("price")
    response = client.get(url)

    assert response.status_code == 200, "Expect 200 response since user is logged in"
    assert not response.context.get("prica")


@pytest.mark.django_db
def test_sve_price_with_messages(auth_client):
    client, user = auth_client
    admin_user = UserFactory(is_staff=True)
    PricaFactory(sender=user)
    PricaFactory(reciever=user, sender=admin_user)

    url = reverse("price")
    response = client.get(url)

    assert response.status_code == 200, "Expect 200 response since user is logged in"
    assert response.context.get("price").count() == 2
