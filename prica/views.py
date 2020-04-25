from django.shortcuts import render
from django.db.models import Q
from .models import PricaModel
from django.views import View
from .forms import PricaForm
from django.contrib.auth.models import User


class MyView(View):
    form = PricaForm

    def get(self, request):
        form = self.form()
        return render(request, 'prica/home.html', {'form': form})

    def post(self, request):
        form = self.form(request.POST)
        admin_user = User.objects.filter(is_superuser=True).first()
        if form.is_valid():
            #user_reciever = User.objects.get(id=request.POST['reciever'])
            PricaModel.objects.create(sender=request.user,
                                      reciever=admin_user,
                                      text=request.POST['text'])
            print('OK')

        return render(request, 'prica/home.html', {'form': self.form()})


class SveView(View):

    def get(self, request):
        price = PricaModel.objects.filter(Q(sender=request.user)
                                          | Q(reciever=request.user))
        return render(request, 'prica/sveprice.html', {'price': price})
