from django.shortcuts import render
from .models import *
from .form import *



def index(request):
    # domain = domainName()
    name = dnspoddomain.objects.values('name')
    context = {'title':'域名系统','domain_name':name}
    return render(request, 'name.html', locals())