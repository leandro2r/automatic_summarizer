# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from models import Summarized
from choices import LANGUAGE_CHOICES
from utils import SummarizeFile
import os

class SubmitSummarizedForm(forms.Form):
	file = forms.CharField(widget=forms.HiddenInput())
	ratio = forms.FloatField(label="Taxa de compressão", 
							 min_value=0, max_value=1, initial=0.5,
							 widget=forms.NumberInput(attrs={"class" : "form-control input-mg", 
									   				   		 "step": "0.01"}))
