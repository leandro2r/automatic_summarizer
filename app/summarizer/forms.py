# -*- coding: utf-8 -*-

from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from models import Summarized
from choices import LANGUAGE_CHOICES
from utils import SummarizeFile
import os

class SubmitSummarizedForm(forms.Form):
	file = forms.CharField(widget=forms.HiddenInput())
	language = forms.ChoiceField(choices=LANGUAGE_CHOICES, 
								label="Idioma do arquivo", 
								widget=forms.Select(attrs={"class" : "form-control input-mg"}))
