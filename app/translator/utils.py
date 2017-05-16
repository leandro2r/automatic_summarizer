# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import io

from textblob import TextBlob

from django.conf import settings
from django.contrib import messages
from app.summarizer.models import Summarized

def ApiTextBlob(text, field):
    blob = TextBlob(text)

    field.from_language = str(blob.detect_language())

    try:
        blob_translated = blob.translate(to=field.to_language)
    except:
        blob_translated = None

    return str(blob_translated)

def TranslateFile(field):
    try:
        from_summarizer = Summarized.objects.get(file_id=field.file.id)
        docfile = str(from_summarizer.summarized_file)
    except Summarized.DoesNotExist:
        docfile = str(field.file.docfile)

    file_path = os.path.join(settings.MEDIA_ROOT, str(docfile))
    new_file = str(docfile).split(".")[0] + "_t.txt"
    new_file_path = os.path.join(settings.MEDIA_ROOT, new_file)

    text = io.open(file_path, encoding="utf8").read()

    content = ApiTextBlob(text, field)

    content = content.decode('utf-8')

    with io.open(new_file_path, "w+", encoding="utf8") as file_txtblob:
        file_txtblob.write(content)

    field.translated_file = new_file
