from django.shortcuts import render
from .models import Prox

def prox(request):
	proxies = Prox.objects
	return render(request, 'proxyapp/proxy.html', {'proxies': proxies})