from django.urls import path

from . import views

urlpatterns = [
    path("", views.AllBlogsView.as_view(), name="allblogs"),
    path("<int:pk>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path("create/", views.AddBlogVew.as_view(), name="create-blog"),
]
