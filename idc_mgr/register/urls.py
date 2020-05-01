from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('visitor', views.visitorRegister, name='visitoregister'),
	path('error', views.registerError, name='registerror'),
	path('success', views.registerSuccess, name='registersuccess'),
]

