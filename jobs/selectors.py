from jobs.models import Job, ClientJobs, Cover
from django.db.models import QuerySet


def jobs_get_jobs() -> "QuerySet[Job]":
    return Job.objects.all()


def jobs_public_client_jobs() -> "QuerySet[ClientJobs]":
    return ClientJobs.objects.filter(all_see=True)


def job_get_cover() -> Cover:
    return Cover.objects.filter(use=True).first()
