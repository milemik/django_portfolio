import factory
from django.contrib.auth import get_user_model

from nalozi.models import Korisnik
from prica.models import PricaModel


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: f"user{n}")
    email = f"{username}@test.com"


class KorisnikFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Korisnik


class PricaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PricaModel

    sender = factory.SubFactory(UserFactory)
    reciever = factory.SubFactory(UserFactory)
