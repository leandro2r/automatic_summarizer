from django.shortcuts import render, redirect
from django import forms
from models import ConvertFile

def index(request):
	files = ConvertFile.objects.all()
	context = {'files':files}
	return render(request, 'convert_app/index.html', context)

def create(request):
	print request.POST
	form = ConvertFile(title=request.POST.get('title'), docfile=request.POST.get('docfile'))
	form.save()
	return redirect('/')
