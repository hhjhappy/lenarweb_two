from django import forms
from django.forms import widgets
from .models import Ops, Visitors, VisitRecord
from django.core.exceptions import ValidationError
#class Visitors(forms.ModelForm):
#   name = forms.CharField(max_length=50, label='名字')
#   opsid = forms.CharField(max_length=20, label='陪同人')
#   class Meta:
#       model = Visitor
#       fields = ("phone",)


class RecordVisit(forms.ModelForm):

    ops = forms.CharField(max_length=20, label="陪同人")
    phone = forms.CharField(max_length=20, label="访客手机号")

    def clean_phone(self):
        cd = self.cleaned_data
        is_exist = Visitors.objects.filter(phone=cd['phone']).exists()
        if not is_exist:
            raise forms.ValidationError("访客未注册")
        else:
            return cd['phone']

    def clean_ops(self):
        cd = self.cleaned_data
        is_exist = Ops.objects.filter(employ_id=cd['ops']).exists()
        if not is_exist:
            raise forms.ValidationError("ops未注册")
        else:
            return cd['ops']

    class Meta:
        model = VisitRecord
        fields = ["reason"]
'''
    def clean_accompany_ops(self):
        accompany_ops = self.cleaned_data["ops"]
        return Ops.objects.get(employ_id=accompany_ops).id
        
    def clean_visitors(self):
        phone = self.cleaned_data["phone"]
'''

class VisitorLeave(forms.ModelForm):
    leavecheck = forms.BooleanField(label=VisitRecord.objects.select_related('visitors').filter(finish=False).values('visitors__name','visit_time'))
    class Meta:
        model = VisitRecord
        fields = ["finish"]

class TestRecord(forms.ModelForm):
    name = forms.CharField(max_length=50, label='名字')
    opsid = forms.CharField(max_length=20, label='陪同人')
    class Meta:
        model = VisitRecord
        fields = ["reason"]
