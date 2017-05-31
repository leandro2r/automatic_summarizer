# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from app.translator.models import File
from utils import AlignFile
import os

class Aligned(models.Model):
	file = models.ForeignKey(File, on_delete=models.CASCADE,
							 null=False, blank=False)
	aligned_file = models.CharField(max_length=100, editable=False)
	sentences_x = models.IntegerField(editable=False)
	sentences_y = models.IntegerField(editable=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		AlignFile(self)
		super(Aligned, self).save()

	def __unicode__(self):
		return self.aligned_file
