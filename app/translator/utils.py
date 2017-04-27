# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import io

from textblob import TextBlob

from django.conf import settings
from app.summarizer.models import Summarized

def ApiTextBlob(text, from_lang, to_lang):
    blob = TextBlob(text)
    blob_translated = blob.translate(from_lang=from_lang, to=to_lang)
    return blob_translated

def TranslateFile(field):
    from_summarizer = Summarized.objects.filter(file_id=field.file.id)

    if from_summarizer:
        docfile = str(from_summarizer.summarized_file)
        doclang = str(from_summarizer.language)
    else:
        docfile = str(field.file.docfile)
        doclang = str("en")

    file_path = os.path.join(settings.MEDIA_ROOT, str(docfile))
    new_file = str(docfile).split(".")[0] + "_t.txt"
    new_file_path = os.path.join(settings.MEDIA_ROOT, new_file)

    text = io.open(file_path, encoding="utf8").read()

    content = ApiTextBlob(text, doclang, field.language)
    print(content)
    # with io.open(new_file_path, "wb", encoding="utf8") as file_txtblob:
    #     file_txtblob.write(content)

    field.translated_file = new_file
