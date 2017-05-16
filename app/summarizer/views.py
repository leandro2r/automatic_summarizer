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
from models import Summarized
from forms import SubmitSummarizedForm

import os
from datetime import datetime

class IndexView(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			messages.error(request, "Nenhum arquivo foi selecionado!")

		return redirect("/")

	def post(self, request, *args, **kwargs):
		method = self.request.POST.get('_method', '').lower()

		file_id = request.POST.get('file', None)
		file = get_object_or_404(File, id=file_id)

		if method == u'converted':
			form = SubmitSummarizedForm(initial={'file': file_id})
			template = "summarizer/index.html"

			context = {
				"title": "Sumarizador",
				"file": file,
				"form": form
			}
			return render(request, template, context)
		else:
			return self.sumarize(request, file, *args, **kwargs)

	def sumarize(self, request, file, *args, **kwargs):
		form = SubmitSummarizedForm(request.POST or None)

		if form.is_valid():
			update = Summarized.objects.filter(file_id=file.id)

			if update:
				summarized = Summarized.objects.get(file_id=file.id)
				summarized.ratio = request.POST['ratio']
			else:
				summarized = Summarized(
					file = file,
					ratio = request.POST['ratio']
				)

			# cleaned data
			ratio = form.cleaned_data["ratio"]

			summarized.save()

			messages.success(request, "O arquivo " + file.title +
							" foi sumarizado com sucesso!")

		file_size = os.stat(os.path.join(settings.MEDIA_ROOT, str(file.docfile)))
		summarized_size = os.stat(os.path.join(settings.MEDIA_ROOT, str(summarized.summarized_file)))
		template = "summarizer/index.html"
		processing_time = datetime.strptime(summarized.processing_time,"%H:%M:%S.%f")

		context = {
			"title": "Sumarizador",
			"file": file,
			"file_size": file_size.st_size,
			"summarized": {
				"field": summarized,
				"size": summarized_size.st_size,
				"processing_time": processing_time
			}
		}
		return render(request, template, context)
