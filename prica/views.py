from django.shortcuts import render
from django.db.models import Q
from .models import PricaModel
from django.views import View
from .forms import PricaForm, AdminPricaForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


class MyView(View):
    form = PricaForm

    def get(self, request):
        if request.user.is_superuser:
            self.form = AdminPricaForm
        form = self.form()
        return render(request, 'prica/home.html', {'form': form})

    def post(self, request):
        if request.user.is_superuser:
            self.form = AdminPricaForm
        form = self.form(request.POST)
        admin_user = User.objects.filter(is_superuser=True).first()
        if form.is_valid():
            # user_reciever = User.objects.get(id=request.POST['reciever'])
            PricaModel.objects.create(sender=request.user,
                                      reciever=admin_user,
                                      text=request.POST['text'])
            message = f'USER: {request.user}\nMESSAGE: {request.POST["text"]}'
            send_mail(
                f'New message from {request.user}',
                message,
                settings.EMAIL_HOST_USER,
                ['pythonscraper@outlook.com'],
                )

        return render(request, 'prica/home.html', {'form': self.form()})


class SveView(View):

    def get(self, request):
        price = PricaModel.objects.filter(Q(sender=request.user)
                                          | Q(reciever=request.user))
        return render(request, 'prica/sveprice.html', {'price': price})
