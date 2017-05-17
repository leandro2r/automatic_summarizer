# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import io
from datetime import datetime

from gensim.summarization import summarize

from django.conf import settings

def Gensim(text, ratio):
    return summarize(text, ratio=ratio, word_count=None, split=False)

def SummarizeFile(field):
    start = datetime.now()
    file_path = os.path.join(settings.MEDIA_ROOT, str(field.file.docfile))
    new_file = str(field.file.docfile).split(".")[0] + "_s.txt"
    new_file_path = os.path.join(settings.MEDIA_ROOT, new_file)

    text = io.open(file_path, encoding="utf8").read()

    content = Gensim(text, float(field.ratio))

    with io.open(new_file_path, "w+", encoding="utf8") as file_text:
        file_text.write(content)

    field.summarized_file = new_file
    field.processing_time = str(datetime.now() - start)
