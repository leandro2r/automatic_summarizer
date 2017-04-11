# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from app.converter.models import File

class IndexView(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			messages.error(request, "Nenhum arquivo foi selecionado!")

		return redirect("/")

	def post(self, request, *args, **kwargs):
		method = self.request.POST.get('_method', '').lower()

		if method == u'translate':
			return self.sumarize(request, *args, **kwargs)

		template = "summarizer/index.html"
		file = File.objects.get(id=request.POST['docfile'])

		context = {
			"title": "Sumarizador",
			"file": file
		}
		return render(request, template, context)

	def sumarize(self, request, *args, **kwargs):
		print "SumySummarizer"
