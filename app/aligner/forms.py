# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from models import Aligned
from utils import AlignFile
import os

class SubmitAlignedForm(forms.Form):
	file = forms.CharField(widget=forms.HiddenInput())
