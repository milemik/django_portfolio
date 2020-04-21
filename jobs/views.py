from django.shortcuts import render
from .models import Job, ClientJobs


def home(request):
    jobs = Job.objects
    client_jobs = ClientJobs.objects.filter(all_see=True)
    return render(request, "jobs/home.html", {'jobs': jobs,
                  'client_jobs': client_jobs})


def about(request):
    return render(request, "jobs/about.html")
