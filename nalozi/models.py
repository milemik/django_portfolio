from django.db import models
from django.conf import settings


class Korisnik(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(default=None)
    about = models.TextField(max_length=500)
