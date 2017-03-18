from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt
import string

def pdf_to_txt(input, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    for page in PDFPage.get_pages(input, pagenums):
        interpreter.process_page(page)
    input.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text 

def convertFile(file):
    pdf = file.name
    fileExtension = pdf.split(".")[-1]
    if fileExtension == "pdf":
        text = pdf_to_txt(file)
    elif fileExtension == "txt":
        text = open(file, 'rb')
        text.close()

    return text