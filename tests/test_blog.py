import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_all_blogs_view(client):
    url = reverse("allblogs")
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_blog_detail_view_blog_doesnt_exist(client):
    url = reverse("blog_detail", args=(1,))
    response = client.get(url)

    assert response.status_code == 404
