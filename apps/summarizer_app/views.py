# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# from apps.converter_app.models import File

class IndexView(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			messages.error(request, "Nenhum arquivo foi selecionado!")

		return redirect("/")

	def post(self, request, *args, **kwargs):
		template = "summarizer_app/index.html"
		# docfile = File.objects.filter(id=request.POST['docfile']).all()

		context = {
			"title": "Sumarizador"
			# "docfile": docfile
		}
		return render(request, template, context)