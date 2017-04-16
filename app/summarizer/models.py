# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.conf import settings

from app.converter.models import File
from choices import LANGUAGE_CHOICES
from utils import SumyFile
import os

class Summarized(models.Model):
	file = models.ForeignKey(File, on_delete=models.CASCADE,
							 null=True, blank=True)
	language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, null=False, blank=False)
	sentences = models.IntegerField(null=False, blank=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		SumyFile(self.file.docfile, self.language, self.sentences)
		# super(Summarized, self).save()

	def __unicode__(self):
		return str(self.file)
