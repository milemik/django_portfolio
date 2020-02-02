from django.shortcuts import render
from .models import Prox

def prox(request):
	proxies = Prox.objects.all()
	if len(proxies) == 0:
		error = 'UPS! SORRY FOR THIS, THIS PAGE IS IN WORKING PROCESS'
	return render(request, 'proxyapp/proxy.html', {'proxies': proxies, 'error': error})