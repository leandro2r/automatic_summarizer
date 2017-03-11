from django.shortcuts import render, redirect
from models import File

def index(request):
	files = File.objects.all()
	context = {'files':files}
	return render(request, 'convert_app/index.html', context)

def create(request):
	print request.POST
	form = File(title=request.POST.get('title'), docfile=request.FILES.get('docfile'))
	form.save()
	return redirect('/')

def edit(request, id):
	file = File.objects.get(id=id)
	context = {"file":file}
	return render(request, 'convert_app/edit.html', context)

def update(request, id):
	file = File.objects.get(id=id)
	file.title = request.POST.get('title')
	file.docfile = request.FILES.get('docfile')
	file.save()
	return redirect('/')

def delete(request, id):
	file = File.objects.get(id=id)
	file.delete()
	return redirect('/')
