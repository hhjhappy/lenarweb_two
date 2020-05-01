from django.urls import path,re_path
from . import views

app_name = 'visitorecord'

urlpatterns = [
    path('', views.visitorecord, name='visitorecord' ),
	path('error', views.visitError, name='visit_error' ),
    #re_path('(?p<recordid>[0-9]{1,9}).html', views.leave, name='visitor_leave'),
]
