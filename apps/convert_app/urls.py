from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
	url(r'^$', views.index), 
	url(r'^create$', views.create),
	url(r'^edit/(?P<id>\d+)$', views.edit),
	url(r'^update/(?P<id>\d+)$', views.update),
	url(r'^delete/(?P<id>\d+)$', views.delete)
]