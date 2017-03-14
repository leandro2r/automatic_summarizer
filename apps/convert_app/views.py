from django.shortcuts import render, redirect
from models import File

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

def index(request):
	files = File.objects.all()
	context = {'files':files}
	return render(request, 'convert_app/index.html', context)

def convert_pdf_to_txt(infile, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text 

def create(request):
	print request.POST
	form = File(title=request.POST.get('title'))
	docfile = request.FILES.get('docfile')
	test = convert_pdf_to_txt(docfile.open('rb'))
	print test

	# form.save()
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
