# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

from app.translator.models import File
from utils import AlignFile
import os

class Aligned(models.Model):
	file = models.ForeignKey(File, on_delete=models.CASCADE,
							 null=False, blank=False)
	aligned_file = models.CharField(max_length=200, editable=False)
	sentences_x = models.IntegerField(editable=False)
	sentences_y = models.IntegerField(editable=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		AlignFile(self)
		super(Aligned, self).save()

	@receiver(pre_delete, sender=File)
	def remove_file(sender, *args, **kwargs):
		try:
			file_id = sender.objects.get().id
			aligned_file = Aligned.objects.get(file_id=file_id).aligned_file
			os.remove(os.path.join(settings.MEDIA_ROOT, aligned_file))
		except:
			pass

	def __unicode__(self):
		return self.aligned_file
