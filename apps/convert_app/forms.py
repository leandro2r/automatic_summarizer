# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ["username", "email", "password"]


class SubmitFileForm(forms.Form):
	title = forms.CharField(label="Título", widget=forms.TextInput(attrs={"class" : "form-control input-lg"}))
	docfile = forms.FileField(label="Arquivo (.pdf)", widget=forms.FileInput(attrs={"class" : "form-control input-lg"}))
	page = forms.CharField(label="Página", initial=1, widget=forms.NumberInput(attrs={"class" : "form-control input-lg"}))
