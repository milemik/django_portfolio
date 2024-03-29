from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import PricaModel
from django.views import View
from .forms import PricaForm, AdminPricaForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


class SendMessage(LoginRequiredMixin, View):
    form = PricaForm

    def get(self, request):
        if request.user.is_superuser:
            self.form = AdminPricaForm
        form = self.form()
        return render(request, "prica/home.html", {"form": form})

    def post(self, request):
        if request.user.is_superuser:
            self.form = AdminPricaForm
        form = self.form(request.POST)
        admin_user = User.objects.filter(is_superuser=True).first()
        if request.user.is_superuser:
            reciever = User.objects.get(id=int(request.POST["reciever"]))
        else:
            reciever = admin_user
        if form.is_valid():
            PricaModel.objects.create(sender=request.user, reciever=reciever, text=request.POST["text"])
            message = f'USER: {request.user}\nMESSAGE: {request.POST["text"]}'
            send_mail(
                f"New message from {request.user}",
                message,
                settings.EMAIL_HOST_USER,
                ["pythonscraper@outlook.com"],
            )
        return render(request, "prica/home.html", {"form": self.form()})


class SveView(LoginRequiredMixin, View):
    def get(self, request):
        price = PricaModel.objects.filter(Q(sender=request.user) | Q(reciever=request.user)).all()
        return render(request, "prica/sveprice.html", {"price": price})


class MarkRead(LoginRequiredMixin, View):
    def post(self, request):
        message = PricaModel.objects.get(id=request.POST.get("message_id"))
        message.is_read = True
        message.save()
        return redirect("price")
