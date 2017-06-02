# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

from app.converter.models import File
from app.translator.models import Translated
from app.translator.choices import LANGUAGE_CHOICES
from models import Aligned
from forms import SubmitAlignedForm

import os

class IndexView(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			messages.error(request, "Nenhum arquivo foi selecionado!")

		return redirect("/")
		
	def post(self, request, *args, **kwargs):
		method = self.request.POST.get('_method', '').lower()

		file_id = request.POST.get('file', None)
		file = get_object_or_404(File, id=file_id)

		if method == u'aligned':
			return self.align(request, file, *args, **kwargs)
		elif method == u'finished':
			aligned = Aligned.objects.get(file_id=file_id)
			response = HttpResponse(aligned.aligned_file, content_type='text/plain')
			response['Content-Disposition'] = 'attachment; filename=' + str(aligned.aligned_file).split("/")[-1]
			return response
		else:
			form = SubmitAlignedForm(initial={'file': file_id})
			template = "aligner/index.html"
			translated = Translated.objects.get(file_id=file_id)

			context = {
				"title": "Alinhador",
				"file": file,
				"form": form,
				"translated": {
					"from_language": dict(LANGUAGE_CHOICES).get(translated.from_language),
					"to_language": dict(LANGUAGE_CHOICES).get(translated.to_language)
				}
			}
			return render(request, template, context)

	def align(self, request, file, *args, **kwargs):
		form = SubmitAlignedForm(request.POST or None)

		if form.is_valid():
			update = Aligned.objects.filter(file_id=file.id)

			if update:
				aligned = Aligned.objects.get(file_id=file.id)
			else:
				aligned = Aligned(
					file = file
				)

			aligned.save()

			messages.success(request, "O arquivo " + file.title +
							" foi alinhado com sucesso!")

		template = "aligner/index.html"

		context = {
			"title": "Alinhador",
			"file": file,
			"aligned": aligned
		}
		return render(request, template, context)
