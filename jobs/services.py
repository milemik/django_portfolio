from django.contrib.auth.models import User

from jobs.models import Job, ClientJobs


def job_create_job(jtitle: str, image: any, description: str) -> None:
    obj = Job.objects.create(
        jtitle=jtitle,
        image=image,
        description=description,
    )
    obj.full_clean()
    obj.save()


def job_create_client_job(client: User, jobtitle: str, jobimage: any, jobdescription: str, all_see: bool) -> None:
    obj = ClientJobs.objects.create(
        client=client,
        jobtitle=jobtitle,
        jobimage=jobimage,
        jobdescription=jobdescription,
        all_see=all_see,
    )
    obj.save()
