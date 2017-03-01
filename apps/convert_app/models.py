# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class File(models.Model):
	title = models.CharField('Título',max_length=100)
	file = models.FileField('Arquivo .PDF')
	url = models.URLField('Repositório', blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)