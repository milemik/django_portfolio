from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.views import View
from .forms import BlogForm
from utils.premissions import SuperUserCheck


def allblogs(request):
    blogs = Blog.objects
    return render(request, "blog/allblogs.html", {'blogs': blogs})


def blog(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blog/blog.html", {'blog': blog_detail})


class AddBlogVew(SuperUserCheck, View):
    form = BlogForm

    def get(self, request):
        form = self.form()
        return render(request, 'blog/createblog.html', {'form': form})

    def post(self, request):
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            obj = Blog.objects.create(
                blog_name=form.cleaned_data.get('title'),
                blog_image=request.FILES['blog_image'],
                blog_description=form.cleaned_data.get('description'),
            )
            obj.save()
            return redirect('allblogs')
        else:
            return render(request, 'blog/createblog.html',
                          {'form': self.form()})
