from django.urls import path

from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.blog, name='blog_detail'),
    path('create/', views.AddBlogVew.as_view(), name='create-blog')
]
