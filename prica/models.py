from django.db import models
from django.conf import settings


class PricaModel(models.Model):

    sender = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='sender')
    reciever = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='reciever')
    text = models.TextField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
    	ordering = ['-time']
