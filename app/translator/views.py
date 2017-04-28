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
from app.summarizer.models import Summarized
from app.summarizer.choices import LANGUAGE_CHOICES as SUMM_LANG_CHOICES
from choices import LANGUAGE_CHOICES as TRANS_LANG_CHOICES
from models import Translated
from forms import SubmitTranslatedForm

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

		if method == u'translated':
			return self.translate(request, file, *args, **kwargs)
		else:
			form = SubmitTranslatedForm(initial={'file': file_id})
			template = "translator/index.html"

			context = {
				"title": "Tradutor",
				"file": file,
				"form": form
			}
			return render(request, template, context)

	def translate(self, request, file, *args, **kwargs):
		form = SubmitTranslatedForm(request.POST or None)

		if form.is_valid():
			update = Translated.objects.filter(file_id=file.id)

			if update:
				translated = Translated.objects.get(file_id=file.id)
				translated.to_language = request.POST['to_language']
			else:
				translated = Translated(
					file = file,
					to_language = request.POST['to_language']
				)

			# cleaned data
			to_language = form.cleaned_data["to_language"]

			translated.save()

			messages.success(request, "O arquivo " + file.title +
							" foi traduzido com sucesso!")

		try:
			Summarized.objects.get(file_id=file.id)
			SUMM_OR_TRANS = SUMM_LANG_CHOICES
		except Summarized.DoesNotExist:
			SUMM_OR_TRANS = TRANS_LANG_CHOICES

		template = "translator/index.html"

		context = {
			"title": "Tradutor",
			"file": file,
			"translated": {
				"from_language": dict(SUMM_OR_TRANS).get(translated.from_language),
				"to_language": dict(TRANS_LANG_CHOICES).get(translated.to_language)
			}
		}
		return render(request, template, context)
