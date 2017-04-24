# -*- coding: utf8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include

from views import IndexView

urlpatterns = [
	url(r'^$', IndexView.as_view(), name="index"),
]
