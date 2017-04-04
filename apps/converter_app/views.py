# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from models import File
from django.contrib.auth.models import User
from forms import UserForm, UserEditForm, SubmitFileForm

class IndexView(View):
	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login/")

		files = File.objects.filter(user=request.user, active=True).all()
		form = SubmitFileForm()
		template = "converter_app/index.html"

		context = {
			"title": "Conversor",
			"form": form,
			"files": files
		}
		return render(request, template, context)

	def post(self, request, *args, **kwargs):
		method = self.request.POST.get('_method', '').lower()

		if method == 'adicionar':
			return self.add(request, *args, **kwargs)
		if method == 'excluir':
			return self.delete(request, *args, **kwargs)


	def add(self, request, *args, **kwargs):
		form = SubmitFileForm(request.POST or None, request.FILES or None)

		if form.is_valid():
			docfile = request.FILES['docfile']
			docfile_ext = docfile.name.split(".")[-1]

			if docfile_ext == "pdf" or docfile_ext == "txt":
				file = File(
					title = request.POST['title'],
					docfile = request.FILES['docfile'],
					page = request.POST['page'],
					user = request.user
				)

				# cleaned data
				title = form.cleaned_data["title"]
				docfile = form.cleaned_data["docfile"]
				page = form.cleaned_data["page"]

				file.save()

				if docfile_ext == "pdf":
					messages.success(request, "O arquivo " + docfile.name +
						" foi convertido para txt e adicionado com sucesso!")
				else:
					messages.success(request, "O arquivo " + docfile.name +
						" foi adicionado com sucesso!")

				form = SubmitFileForm()
			else:
				messages.error(request, "Formato do arquivo ." + docfile_ext +
					u" inválido! Apenas .pdf e .txt são permitidos.")

		files = File.objects.filter(user=request.user).all()
		template = "converter_app/index.html"
		context = {
			"title": "Conversor",
			"form": form,
			"files": files
		}
		return render(request, template, context)

	def delete(self, request, *args, **kwargs):
		files = request.POST.getlist("delete_ids")
		for each in files:
			form = File.objects.filter(id=each).delete()

		n_files = len(files)
		if n_files > 1:
			messages.success(request, "Os " + str(n_files) +
				" arquivos selecionados foram removidos com sucesso!")
		else:
			messages.success(request, "O arquivo selecionado foi removido"
				" com sucesso!")
		return redirect('/')

class UserView(View):
	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			form = UserForm()
			title = "Registrar"
			template = "apps/register.html"
		else:
			form = UserEditForm(instance=request.user)
			title = "Editar"
			template = "apps/edit.html"

		context = {
			"title": title,
			"form": form
		}
		return render(request, template, context)

	def post(self, request, *args, **kwargs):
		method = self.request.POST.get('_method', '').lower()

		if not request.user.is_authenticated():
			form = UserForm(request.POST)
			return self.new(request, form, *args, **kwargs)
		else:
			form = UserEditForm(request.POST)
			return self.edit(request, form, *args, **kwargs)

	def new(self, request, form, *args, **kwargs):
		if form.is_valid():
			if request.POST['password'] == request.POST['confirm_password']:
				user = form.save(commit=False)

				# cleaned data
				username = form.cleaned_data["username"]
				email = form.cleaned_data["email"]
				password = form.cleaned_data["password"]

				user.set_password(password)
				user.save()

				user = authenticate(username=username, password=password)

				if user is not None:
					if user.is_active:
						login(request, user)
						messages.success(request, u"Usuário " + user.username +
							" registrado com sucesso! Seja bem-vindo(a)")
						return redirect("/")
			else:
				messages.error(request,
					"A senha informada diverge da senha de confirmação. Verifique-as")

		context = {
			"title": "Registrar",
			"form": form
		}
		return render(request, "apps/register.html", context)

	def edit(self, request, form, *args, **kwargs):
		if form.is_valid():
			user = form.save(commit=False)

			# cleaned data
			email = form.cleaned_data["email"]
			password = form.cleaned_data["password"]

			# if request.POST['password'] == request.POST['confirm_password']
			# 	and request.POST['password'] is not None:
			# 	user.set_password(password)
			# 	user.save()

			messages.success(request, u"Usuário " + user.username +
				" editado com sucesso!")

		context = {
			"title": "Editar",
			"form": form
		}
		return render(request, "apps/edit.html", context)
