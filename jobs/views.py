from django.shortcuts import render, redirect
from .models import Job, ClientJobs, Cover
from .forms import JobForm, ClientJobsForm
from django.views import View
from utils.premissions import SuperUserCheck
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    jobs = Job.objects
    client_jobs = ClientJobs.objects.filter(all_see=True)
    cover_image = Cover.objects.filter(use=True).first().cover_image
    return render(request, "jobs/home.html", {"jobs": jobs, "client_jobs": client_jobs, "cover": cover_image})


def about(request):
    return render(request, "jobs/about.html")


class AddJobView(SuperUserCheck, View):
    form = JobForm

    def get(self, request):
        form = self.form()
        return render(request, "jobs/createjob.html", {"form": form})

    def post(self, request):
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            obj = Job.objects.create(
                jtitle=form.cleaned_data.get("title"),
                image=request.FILES["image_form"],
                description=form.cleaned_data.get("description"),
            )
            obj.save()
            return redirect("home")
        else:
            return render(request, "jobs/createjob.html", {"form": self.form()})


class ClientJobView(LoginRequiredMixin, View):

    form = ClientJobsForm
    login_url = "login"

    def get(self, request):
        form = self.form()
        return render(request, "jobs/createjob.html", {"form": form})

    def post(self, request):
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            obj = ClientJobs.objects.create(
                client=request.user,
                jobtitle=form.cleaned_data.get("jobtitle"),
                jobimage=request.FILES["jobimage"],
                jobdescription=form.cleaned_data.get("jobdescription"),
                all_see=form.cleaned_data.get("all_see"),
            )
            obj.save()
            return redirect("profile")
        else:
            return render(request, "jobs/createjob.html", {"form": self.form()})
