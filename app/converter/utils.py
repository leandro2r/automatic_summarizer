# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import io
import os
import sys, getopt
import string

from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

from django.core.files.base import ContentFile
from django.conf import settings

def pdf_to_txt(input, pages):
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

def format_content(content):
    content = content.decode("utf-8")

    clean_text = re.sub(r"(\d\s*)([A-Z].*)", 
                        r"--LINEBREAK----LINEBREAK-- \2 --LINEBREAK--", 
                        content)
    clean_text = re.sub(r"(\S)(\s*\n)", r"\1 ", clean_text)
    clean_text = re.sub(r"\d?\s\n{2,}", "", clean_text)
    clean_text = clean_text.replace("--LINEBREAK--", "\n")

    return clean_text.encode("utf-8")

def ConvertFile(field):
    file = field.docfile
    file_name = file.name
    fileExtension = file_name.split(".")[-1]

    if fileExtension == "pdf":
        if field.starts_at and field.ends_at:
            starts_at = int(field.starts_at)
            ends_at = int(field.ends_at)

            pages = range(starts_at - 1, ends_at - 1)
        else:
            pages = None

        newcontent = pdf_to_txt(file, pages)
        newdocfile = os.path.splitext(os.path.basename(file_name))[0] + ".txt"

        newcontent = format_content(newcontent)
        file.save(newdocfile, ContentFile(newcontent))
    elif fileExtension == "txt":
        content = file.read()

        try:
            newcontent = content.decode('utf-8')
        except:
            newcontent = content.decode('ISO-8859-1').encode('utf-8')
            file.save(file_name, ContentFile(newcontent))            
