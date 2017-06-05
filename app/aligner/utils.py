# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import io
import re
import csv
from itertools import izip

from app.translator.models import Translated
from app.summarizer.models import Summarized

from django.conf import settings

from galechurch import read_blocks, align

def GaleAndChurch(corpus_x, corpus_y, file):
	sentences = [0,0]

	with open(file, "w+") as file_galechurch:
		with open(corpus_x) as fx, open(corpus_y) as fy:
			file_writer = csv.DictWriter(file_galechurch, 
				fieldnames=["Sumarizado", "Traduzido"], delimiter=str("|"))
			file_writer.writeheader()

			for block_x, block_y in izip(read_blocks(fx), read_blocks(fy)):
				for (sentence_x, sentence_y) in align(block_x, block_y):
					file_writer.writerow({"Sumarizado": sentence_x, "Traduzido": sentence_y})

				sentences[0] = len(block_x)
				sentences[1] = len(block_y)

	return sentences

def AlignFile(field):
	try:
		from_summarizer = Summarized.objects.get(file_id=field.file.id)
		docfile = str(from_summarizer.summarized_file)
	except Summarized.DoesNotExist:
		docfile = str(field.file.docfile)

	files = Translated.objects.get(file_id=field.file.id)

	file_path = os.path.join(settings.MEDIA_ROOT, str(docfile))
	translated = os.path.join(settings.MEDIA_ROOT, str(files.translated_file))
	new_file = str(translated).split(".")[0] + "_a.csv"
	new_file_path = os.path.join(settings.MEDIA_ROOT, new_file)

	sentences = GaleAndChurch(file_path, translated, new_file_path);

	field.sentences_x = sentences[0]
	field.sentences_y = sentences[1]

	field.aligned_file = new_file
