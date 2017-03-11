# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

def validate_file_ext(value):
 	import os
	ext = os.path.splitext(value.name)[1]
	valid_extensions = ['.pdf','.txt']
	if not ext in valid_extensions:
		raise ValidationError(u'File not supported!')

class File(models.Model):
	title = models.CharField(max_length=100)
	docfile = models.FileField(upload_to='files/', validators=[validate_file_ext])
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.title)