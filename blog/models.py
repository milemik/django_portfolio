from django.db import models

# Create your models here.

class Blog(models.Model):
	# Dodavalje slike u bazu podataka
	blog_name = models.CharField(max_length=20)
	blog_date = models.DateTimeField()
	blog_image = models.ImageField(upload_to='images/')
	# opis posla
	blog_description = models.TextField()

	def blog_text():
		tex = f"{self.blog_description[:100]}..."

	def __str__(self):
		return self.blog_name
