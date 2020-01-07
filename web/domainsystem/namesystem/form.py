from django import forms
from .models import *

# class domainName(forms.Form):
    # domainname = forms.CharField(max_length=20,widget=forms.widgets.Select(attrs={'class':'type','size':'4'}))
    # nameList = [ i for i in dnspoddomain.objects.values('name')]
    # name = forms.ChoiceField(choices=nameList,label='域名列表')
    # name = forms.CharField
