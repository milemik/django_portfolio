from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class Job(models.Model):
    jtitle = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    description = models.TextField()

    def __str__(self):
        return self.jtitle

    class Meta:
        ordering = ["-id"]


class ClientJobs(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    jobtitle = models.CharField(max_length=100)
    jobimage = models.ImageField(upload_to="images/")
    jobdescription = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    all_see = models.BooleanField()

    class Meta:
        ordering = ["-date_time"]


class Cover(models.Model):
    cover_title = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to="images/cover")
    use = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.cover_title

    class Meta:
        ordering = ["id"]
