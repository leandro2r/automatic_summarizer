# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

from app.converter.models import File
from choices import LANGUAGE_CHOICES
from utils import SummarizeFile
import os

class Summarized(models.Model):
	file = models.ForeignKey(File, on_delete=models.CASCADE,
							 null=False, blank=False)
	summarized_file = models.CharField(max_length=100, editable=False)
	ratio = models.FloatField(default=0.5, validators = [MinValueValidator(0.01), MaxValueValidator(0.99)], null=False, blank=False)
	processing_time = models.TimeField(editable=False, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		SummarizeFile(self)
		super(Summarized, self).save()

	def __unicode__(self):
		return self.summarized_file
