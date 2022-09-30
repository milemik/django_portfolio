import pytest
from django.urls import reverse

from blog.models import Blog
from tests.factories import BlogFactory, UserFactory


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


@pytest.mark.django_db
def test_blog_detail_view_blog_exist(client):
    blog = BlogFactory()
    url = reverse("blog_detail", args=(blog.id,))
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_blog_create_view_not_superuser(client):
    url = reverse("create-blog")
    response = client.post(url, follow=True)

    assert response.status_code == 404


@pytest.mark.django_db
def test_blog_create_view_not_superuser(client):
    url = reverse("create-blog")
    response = client.get(url, follow=True)

    assert response.status_code == 404


@pytest.mark.django_db
def test_blog_create_view_is_superuser_empty(client):
    url = reverse("create-blog")
    user = UserFactory(is_superuser=True)
    client.force_login(user=user)
    response = client.get(url, follow=True)

    assert response.status_code == 200


@pytest.mark.django_db
def test_blog_create_view_is_superuser(client):
    url = reverse("create-blog")
    user = UserFactory(is_superuser=True)
    blog = BlogFactory()
    client.force_login(user=user)
    response = client.post(url, data={
        "title": "testing",
        "blog_image": blog.blog_image,
        "description": "some description here"
    }, follow=True)

    assert response.status_code == 200
    assert Blog.objects.all().count() == 2
