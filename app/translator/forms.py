# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from models import Translated
from choices import LANGUAGE_CHOICES
from utils import TranslateFile
import os

class SubmitTranslatedForm(forms.Form):
	file = forms.CharField(widget=forms.HiddenInput())
	to_language = forms.ChoiceField(choices=LANGUAGE_CHOICES, 
								label="Idioma da tradução", 
								widget=forms.Select(attrs={"class" : "form-control input-mg"}))
