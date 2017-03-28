from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import IndexView, UserView

urlpatterns = [
	url(r'^$', IndexView.as_view(), name="index"), 
	url(r'^register/$', UserView.as_view(), name="register"), 
	url(r'^login/$', auth_views.login, {'template_name': 'convert_app/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
]
