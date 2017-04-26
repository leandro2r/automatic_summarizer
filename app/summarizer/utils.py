# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import io

from pyteaser import Summarize

from django.conf import settings

def PyTeaser(title, text):
    return Summarize(title, text)

def SummarizeFile(field):
    file_path = os.path.join(settings.MEDIA_ROOT, str(field.file.docfile))
    new_file = str(field.file.docfile).split(".")[0] + "_s.txt"
    new_file_path = os.path.join(settings.MEDIA_ROOT, new_file)

    text = io.open(file_path, encoding="utf8").read()

    content = PyTeaser(field.file.title, text)

    with io.open(new_file_path, "w+", encoding="utf8") as file_pyt:
        for sentences in content:
            file_pyt.write(sentences)

    field.summarized_file = new_file
    field.sentences = len(content)
