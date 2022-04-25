import pytest
from django.urls import reverse

from tests.factories import ClientJobsFactory


@pytest.mark.django_db
def test_profile(auth_client):
    client, user = auth_client
    url = reverse("profile")
    response = client.get(url)

    assert response.status_code == 200, "Expect OK response"
    assert not response.context["jobs"], "Expect jobs queryset is empty"


@pytest.mark.django_db
def test_profile_with_job(auth_client):
    client, user = auth_client
    ClientJobsFactory(client=user)
    ClientJobsFactory()
    url = reverse("profile")
    response = client.get(url)

    assert response.status_code == 200, "Expect OK response"
    assert response.context["jobs"].count() == 1, "Expect jobs queryset shows 1 job"



@pytest.mark.django_db
def test_profile_admin(admin_client):
    job_num = 3
    client, user = admin_client
    ClientJobsFactory.create_batch(job_num)
    url = reverse("profile")
    response = client.get(url)

    assert response.status_code == 200, "Expect OK response"
    assert response.context["jobs"].count() == job_num, "Expect jobs queryset show all jobs"

