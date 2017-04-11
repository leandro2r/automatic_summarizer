# -*- coding: utf8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

def SumySummarizer(file, language):
	SENTENCES_COUNT = 10
    parser = PlaintextParser.from_file(file, Tokenizer(language))
    stemmer = Stemmer(language)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(language)

    file = open("new_file.txt","w") 

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        file.write(sentence)

    file.close()
