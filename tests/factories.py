import factory
from django.contrib.auth import get_user_model

from blog.models import Blog
from jobs.models import ClientJobs
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


class PricaModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PricaModel

    sender = factory.SubFactory(UserFactory)
    reciever = factory.SubFactory(UserFactory)


class ClientJobsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ClientJobs

    client = factory.SubFactory(UserFactory)
    all_see = False
    jobimage = factory.django.ImageField()


class BlogFactory(factory.django.DjangoModelFactory):
    blog_image = factory.django.ImageField()
    class Meta:
        model = Blog
