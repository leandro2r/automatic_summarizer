# -*- coding: utf8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

import os

from django.conf import settings

def SumyFile(file, new_file, language, sentences_count):
    parser = PlaintextParser.from_file(file, Tokenizer(language))
    stemmer = Stemmer(language)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(language)

    sumy = open(new_file, "w") 

    for sentence in summarizer(parser.document, sentences_count):
        sumy.write(sentence)

    sumy.close()

def SummarizeFile(field):
	file_path = os.path.join(settings.MEDIA_ROOT, str(field.file.docfile))
	new_file = str(field.file.docfile).split(".")[0] + "_s.txt"
	new_file_path = os.path.join(settings.MEDIA_ROOT, new_file)

	SumyFile(file_path, new_file_path, field.language, field.sentences)

	field.summarized_file = new_file
