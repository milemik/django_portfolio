from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.views import View
from django.views.generic import TemplateView, DetailView
from .forms import BlogForm
from utils.premissions import SuperUserCheck


class AllBlogsView(TemplateView):
    template_name = "blog/allblogs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"] = Blog.objects.all()
        return context


class BlogDetailView(DetailView):
    template_name = "blog/blog.html"

    queryset = Blog.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog"] = self.get_object()
        return context


class AddBlogVew(SuperUserCheck, View):
    form = BlogForm

    def get(self, request):
        form = self.form()
        return render(request, "blog/createblog.html", {"form": form})

    def post(self, request):
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            obj = Blog.objects.create(
                blog_name=form.cleaned_data.get("title"),
                blog_image=request.FILES["blog_image"],
                blog_description=form.cleaned_data.get("description"),
            )
            obj.save()
            return redirect("allblogs")
        else:
            return render(request, "blog/createblog.html", {"form": self.form()})
