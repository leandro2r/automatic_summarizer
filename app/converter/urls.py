# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include

from views import IndexView, UserView

urlpatterns = [
	url(r'^$', IndexView.as_view(), name="index"),
	url(r'^register/', UserView.as_view(), name="register"),
	url(r'^edit/', UserView.as_view(), name="edit"),
	url(r'^summarizer/', include('app.summarizer.urls')),
	url(r'^translator/', include('app.translator.urls')),
	url(r'^aligner/', include('app.aligner.urls')),
]
