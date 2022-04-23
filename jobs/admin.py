from django.contrib import admin

from .models import Job, ClientJobs, Cover

admin.site.register(Job)
admin.site.register(ClientJobs)
admin.site.register(Cover)
