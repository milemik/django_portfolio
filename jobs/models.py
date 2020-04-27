from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here
# DATABASE!!!!!
# U dokumentaciji django model field refere


class Job(models.Model):
    # Naziv
    jtitle = models.CharField(max_length=100)
    # Dodavalje slike u bazu podataka
    image = models.ImageField(upload_to='images/')
    # opis posla
    description = models.TextField()

    def __str__(self):
        return self.jtitle

    class Meta:
        ordering = ['-id']


class ClientJobs(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL,
                               unique=True,
                               on_delete=models.CASCADE)
    jobtitle = models.CharField(max_length=100)
    # Dodavalje slike u bazu podataka
    jobimage = models.ImageField(upload_to='images/')
    # opis posla
    jobdescription = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    all_see = models.BooleanField()

    class Meta:
        ordering = ['-date_time']
