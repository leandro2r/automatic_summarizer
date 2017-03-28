# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django import forms

from .utils import ConvertFile
import os 

class UserForm(forms.ModelForm):
	username = forms.CharField(label="Usuário", widget=forms.TextInput(attrs={"class" : "form-control input-mg"}))
	email = forms.EmailField(widget=forms.TextInput(attrs={"class" : "form-control input-mg"}))
	password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={"class" : "form-control input-mg"}))

	class Meta:
		model = User
		fields = ["username", "email", "password"]


class SubmitFileForm(forms.Form):
	title = forms.CharField(label="Título", widget=forms.TextInput(attrs={"class" : "form-control input-mg"}))
	docfile = forms.FileField(label="Arquivo (.pdf)", widget=forms.FileInput(attrs={"class" : "form-control input-mg"}))
	page = forms.CharField(label="Página", initial=1, widget=forms.NumberInput(attrs={"class" : "form-control input-mg"}))
	active = forms.BooleanField(initial=True, widget=forms.HiddenInput())
