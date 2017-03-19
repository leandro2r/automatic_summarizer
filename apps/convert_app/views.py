from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View 
from django.contrib.auth import authenticate, login

from models import File
from forms import UserForm, SubmitFileForm

class IndexView(View):
	def get(self, request, *args, **kwargs):
		files = File.objects.all()
		form = SubmitFileForm()

		context = {
			"title": "Conversor",
			"form": form,
			"files": files
		}
		return render(request, "convert_app/index.html", context)

	def post(self, request, *args, **kwargs):
		files = File.objects.all()
		form = SubmitFileForm(request.POST)

		if form.is_valid():
			file = form.save(commit=False)

			# cleaned data
			title = form.cleaned_data["title"]
			docfile = form.cleaned_data["docfile"]
			page = form.cleaned_data["page"]

			file.save()

		context = {
			"title": "Project",
			"form": form,
			"files": files
		}
		return render(request, "convert_app/index.html", context)

class UserView(View):
	def get(self, request, *args, **kwargs):
		form = UserForm()

		context = {
			"title": "Login",
			"form": form
		}
		return render(request, "convert_app/register.html", context)

	def post(self, request, *args, **kwargs):
		form = UserForm(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			# cleaned data
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]

			user.set_password(password)
			user.save()

			user = authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect("/")

		context = {
			"title": "Project login",
			"form": form
		}
		return render(request, "convert_app/register.html", context)
