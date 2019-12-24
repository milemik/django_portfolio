from django.db import models

# Create your models here
# DATABASE!!!!!
# U dokumentaciji django model field refere

class Job(models.Model):
	# Dodavalje slike u bazu podataka
	image = models.ImageField(upload_to='images/')
	# opis posla
	description = models.CharField(max_length=200)
