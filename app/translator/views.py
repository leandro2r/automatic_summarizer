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
from models import Translated
from forms import SubmitTranslatedForm

import os

class IndexView(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			messages.error(request, "Nenhum arquivo foi selecionado!")

		return redirect("/")
		
	def post(self, request, *args, **kwargs):
		print("entrou!")
		method = self.request.POST.get('_method', '').lower()

		file_id = request.POST.get('file', None)
		file = get_object_or_404(File, id=file_id)

		form = SubmitTranslatedForm(initial={'file': file_id})
		template = "translator/index.html"

		context = {
			"title": "Tradutor",
			"file": file,
			"form": form
		}
		return render(request, template, context)

