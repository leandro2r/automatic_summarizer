from django.shortcuts import render, redirect
from models import File

def index(request):
	files = File.objects.all()
	context = {'files':files}
	return render(request, 'convert_app/index.html', context)

def create(request):
	form = File(request.POST)
	form.save()
	return redirect('/')
