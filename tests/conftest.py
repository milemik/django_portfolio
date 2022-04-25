import pytest
from django.test import Client

from tests.factories import UserFactory


@pytest.fixture
def auth_client():
    user = UserFactory()
    client = Client()
    client.force_login(user)
    return client, user


@pytest.fixture
def admin_client():
    admin_user = UserFactory(is_staff=True, is_superuser=True)
    client = Client()
    client.force_login(admin_user)
    return client, admin_user
