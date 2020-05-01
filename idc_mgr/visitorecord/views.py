from django.shortcuts import render,redirect
from .forms import RecordVisit, VisitorLeave
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def visitorecord(request):

	if request.method == 'GET':
		recordvisit = RecordVisit()
		in_room = VisitRecord.objects.select_related('visitors').filter(finish=False).values('visitors__name','visit_time','id','visitors__company')
		return render(request, 'visitorecord/visitorecord.html', locals())
	else:
		recordvisit = RecordVisit(request.POST)
		finish_list = request.POST.getlist("checkbox", None)

		if recordvisit.is_valid():
			record = recordvisit.save(commit=False)
			record.accompany_ops = Ops.objects.get(employ_id=recordvisit.cleaned_data["ops"])
			record.visitors = Visitors.objects.get(phone=recordvisit.cleaned_data["phone"])
			record.save()
			return redirect('/visitorecord')
		elif finish_list:
			for id in finish_list:
#			VisitRecord.objects.filter(id=id).update(finish=True)
				record = VisitRecord.objects.get(id=id)
				record.finish = True
				record.save()	
				return redirect('/visitorecord')
		else:
			return HttpResponseRedirect('error')

def visitError(request):
    if request.method == "GET":
        return render(request, "visitorecord/error.html")
