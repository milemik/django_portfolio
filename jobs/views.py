from typing import Dict

from django.shortcuts import render, redirect
from .models import Job, ClientJobs, Cover
from .forms import JobForm, ClientJobsForm
from django.views import View
from utils.premissions import SuperUserCheck
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView

from .selectors import jobs_get_jobs, jobs_public_client_jobs, job_get_cover


class HomeView(TemplateView):
    template_name = "jobs/home.html"

    def get_context_data(self, **kwargs) -> Dict:
        context = super().get_context_data(**kwargs)
        context["jobs"] = jobs_get_jobs()
        context["client_jobs"] = jobs_public_client_jobs()
        context["cover"] = job_get_cover().cover_image
        return context


class AboutView(TemplateView):
    template_name = "jobs/about.html"


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
