# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import io
import re
from itertools import izip

from app.translator.models import Translated

from django.conf import settings

from galechurch import read_blocks, align

def GaleAndChurch(corpus_x, corpus_y):
	content = ""

	with open(corpus_x) as fx, open(corpus_y) as fy:
		for block_x, block_y in izip(read_blocks(fx), read_blocks(fy)):
			for (sentence_x, sentence_y) in align(block_x, block_y):
				content += sentence_x.decode('utf-8') + "\n|||\n" + sentence_y.decode('utf-8') + "\n\n------------------------\n\n"

	return content

def AlignFile(field):
	files = Translated.objects.get(file_id=field.file.id)

	docfile = os.path.join(settings.MEDIA_ROOT, str(field.file.docfile))
	translated = os.path.join(settings.MEDIA_ROOT, str(files.translated_file))
	new_file = str(docfile).split(".")[0] + "_a.txt"
	new_file_path = os.path.join(settings.MEDIA_ROOT, new_file)

	content = GaleAndChurch(docfile, translated);

	with io.open(new_file_path, "w+", encoding="utf-8") as file_galechurch:
		file_galechurch.write(content)

	sentences_x = re.findall(r"[^\n]\n\|{3}", content)
	sentences_y = re.findall(r"\|{3}\n[^\n]", content)

	field.sentences_x = len(sentences_x)
	field.sentences_y = len(sentences_y)

	field.aligned_file = new_file
