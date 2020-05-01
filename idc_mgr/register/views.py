from django.shortcuts import render, redirect
from .forms import VisitorRegister
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def visitorRegister(request):
	if request.method == 'GET':
		visitoregister = VisitorRegister()
		return render(request, 'register/visitoregister.html', locals())

	else:
		visitoregister = VisitorRegister(request.POST)
		if visitoregister.is_valid():
			new_visitor = visitoregister.save(commit=False)
			new_visitor.save()
			return HttpResponseRedirect('success')
		else:
#            return HttpResponse('注册失败，请重新返回注册页面')
			return HttpResponseRedirect('error')

def registerError(request):
	if request.method == 'GET':
		return render(request, 'register/error.html')

def registerSuccess(request):
    if request.method == 'GET':
        return render(request, 'register/success.html')
