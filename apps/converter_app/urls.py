from django.conf.urls import url, include

from .views import IndexView, UserView

urlpatterns = [
	url(r'^$', IndexView.as_view(), name="index"),
	url(r'^register/', UserView.as_view(), name="register"),
	url(r'^edit/', UserView.as_view(), name="edit"),
	url(r'^summarizer/', include('apps.summarizer_app.urls')),
]
