from django import forms
from visitorecord.models import Visitors

class VisitorRegister(forms.ModelForm):
    class Meta:
        model = Visitors
        fields = '__all__'
