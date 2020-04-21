from django.contrib import admin

from .models import Job, ClientJobs

admin.site.register(Job)
admin.site.register(ClientJobs)