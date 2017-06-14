# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

from app.converter.models import File
from choices import LANGUAGE_CHOICES
from utils import TranslateFile
import os

class Translated(models.Model):
	file = models.ForeignKey(File, on_delete=models.CASCADE,
							 null=False, blank=False)
	from_language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, editable=False)
	to_language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, null=False, blank=False)
	translated_file = models.CharField(max_length=200, editable=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		TranslateFile(self)
		super(Translated, self).save()

	@receiver(pre_delete, sender=File)
	def remove_file(sender, *args, **kwargs):
		try:
			file_id = sender.objects.first().id
			translated_file = Translated.objects.get(file_id=file_id).translated_file
			os.remove(os.path.join(settings.MEDIA_ROOT, translated_file))
		except:
			pass

	def __unicode__(self):
		return self.translated_file
