from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View 
from django.contrib import auth, messages

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
		# if not request.user.is_authenticated():
		# 	raise Http404

		files = File.objects.all()
		form = SubmitFileForm(request.POST or None, request.FILES or None)

		if form.is_valid():
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

			messages.success(request, "Upload de arquivo efetuado com sucesso!")

		context = {
			"title": "Conversor",
			"form": form,
			"files": files
		}
		return render(request, "convert_app/index.html", context)

class UserView(View):
	def get(self, request, *args, **kwargs):
		form = UserForm()

		context = {
			"title": "Registrar",
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

			user = auth.authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					auth.login(request, user)
					return redirect("/")

		context = {
			"title": "Login",
			"form": form
		}
		return render(request, "convert_app/register.html", context)
