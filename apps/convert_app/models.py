# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class File(models.Model):
	title = models.CharField(max_length=100)
	file = models.FileField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.title)