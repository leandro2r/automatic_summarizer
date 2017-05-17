# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from utils import ConvertFile
import os

class File(models.Model):
	title = models.CharField(max_length=100, null=False, blank=False)
	docfile = models.FileField(upload_to="files/", null=False, blank=False)
	is_summarized = models.BooleanField(default=False)
	starts_at = models.DecimalField(max_digits=3, decimal_places=0, null=True)
	ends_at = models.DecimalField(max_digits=3, decimal_places=0, null=True)
	is_active = models.BooleanField(default=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		ConvertFile(self)
		super(File, self).save()

	def __unicode__(self):
		return self.title
