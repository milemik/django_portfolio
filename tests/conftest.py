import pytest
from django.test import Client

from tests.factories import UserFactory


@pytest.fixture
def auth_client():
    user = UserFactory()
    client = Client()
    client.force_login(user)
    return client, user
