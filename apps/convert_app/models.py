# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

from .utils import convertFile
from django.core.files.base import ContentFile
import os

class ConvertFile(models.Model):
	title = models.CharField('title', max_length=100)
	docfile = models.FileField('docfile', upload_to='files/', null=False, blank=False)
	page = models.DecimalField(max_digits=2, decimal_places=0, default='1')
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		newcontent = convertFile(self.docfile)
		newdocfile = os.path.splitext(os.path.basename(self.docfile.name))[0] + ".txt"
		self.docfile.save(newdocfile, ContentFile(newcontent))
		super(ConvertFile, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.title)

	def __unicode__(self):
		return str(self.title)