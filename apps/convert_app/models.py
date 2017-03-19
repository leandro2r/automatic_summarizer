# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

from .utils import ConvertFile
import os 

class File(models.Model):
	title = models.CharField(max_length=100, null=False, blank=False)
	docfile = models.FileField(upload_to="files/", null=False, blank=False)
	page = models.DecimalField(max_digits=2, decimal_places=0, default="1")
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		ConvertFile(self.docfile)
		super(File, self).save()

	def __unicode__(self):
		return str(self.title)
		