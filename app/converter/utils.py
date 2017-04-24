# -*- coding: utf8 -*-

import os
import sys, getopt
import string

from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

from django.core.files.base import ContentFile

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

def ConvertFile(file):
    pdf = file.name
    fileExtension = pdf.split(".")[-1]
    if fileExtension == "pdf":
        newcontent = pdf_to_txt(file)
        newdocfile = os.path.splitext(os.path.basename(pdf))[0] + ".txt"
        file.save(newdocfile, ContentFile(newcontent))
