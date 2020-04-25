from django.shortcuts import render
from .models import Job, ClientJobs
from .forms import JobForm
from django.views import View
from utils.premissions import SuperUserCheck


def home(request):
    jobs = Job.objects
    client_jobs = ClientJobs.objects.filter(all_see=True)
    return render(request, "jobs/home.html", {'jobs': jobs,
                  'client_jobs': client_jobs})


def about(request):
    return render(request, "jobs/about.html")


class AddJobView(SuperUserCheck, View):
    form = JobForm

    def get(self, request):
        form = self.form()
        return render(request, 'jobs/createjob.html', {'form': form})

    def post(self, request):
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            obj = Job.objects.create(
                jtitle=form.cleaned_data.get('title'),
                image=request.FILES['image_form'],
                description=form.cleaned_data.get('description')
                )
            obj.save()

        return render(request, 'jobs/createjob.html', {'form': self.form()})
