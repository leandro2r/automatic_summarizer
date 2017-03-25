from django.conf.urls import url

from .views import IndexView, UserView

urlpatterns = [
	url(r'^$', IndexView.as_view(), name="index"), 
	url(r'^login/$', UserView.as_view(), name="login"), 
	url(r'^register/$', UserView.as_view(), name="register"), 
]
