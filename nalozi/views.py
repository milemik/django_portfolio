from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm
from .models import Korisnik
from jobs.models import ClientJobs
from django.core.mail import send_mail
from django.conf import settings

MAINTENANCE_HTML = "maintenance_profile.html"


def maintenance(request):
    """User only to put some page/view under maintenance!"""
    return render(request, MAINTENANCE_HTML)


def singup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                f"WEBSITE: New registrated user!",
                "New user registration on your website",
                settings.EMAIL_HOST_USER,
                ["pythonscraper@outlook.com"],
            )

            return redirect("login")
    else:
        form = SignupForm()
    return render(
        request,
        "singup.html",
        {
            "form": form,
        },
    )


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html", {"form": form, "message": "UPS! Wrong username or pass"})
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})


@login_required
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    else:
        return render(request, "logout.html")


@login_required
def profile(request):
    try:
        info = Korisnik.objects.filter(user=request.user).first()
        jobs = ClientJobs.objects.filter(client=request.user)
        return render(request, "profil.html", {"info": info, "jobs": jobs})
    except TypeError:
        return redirect("singup")


@login_required
def delete_user(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        return redirect("home")
    else:
        raise ValueError("Request method not allowed!")
