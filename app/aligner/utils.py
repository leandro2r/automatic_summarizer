# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import io
from itertools import izip

from app.translator.models import Translated

from django.conf import settings

from galechurch import read_blocks, align

def GaleAndChurch(original, translated):
	content = ""

	for block_x, block_y in izip(read_blocks(original), read_blocks(translated)):
		for (sentence_x, sentence_y) in align(block_x, block_y):
			content += sentence_x + "|||" + sentence_y + "\n"

	return content


def AlignFile(field):
	files = Translated.objects.get(file_id=field.file.id)

	docfile = os.path.join(settings.MEDIA_ROOT, str(field.file.docfile))
	translated = os.path.join(settings.MEDIA_ROOT, str(files.translated_file))
	new_file = str(docfile).split(".")[0] + "_a.txt"
	new_file_path = os.path.join(settings.MEDIA_ROOT, new_file)

	try:
		corpus_x = io.open(docfile, encoding="utf-8").read()
	except:
		corpus_x = io.open(docfile, encoding="ISO-8859-1").read()

	try:
		corpus_y = io.open(translated, encoding="utf-8").read()
	except:
		corpus_y = io.open(translated, encoding="ISO-8859-1").read()

	content = GaleAndChurch(corpus_x, corpus_y);

	content = content.decode('utf-8')

	with io.open(new_file_path, "w+", encoding="utf8") as file_galechurch:
		file_galechurch.write(content)

	field.aligned_file = new_file
