# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm 

from models import File
from .utils import ConvertFile
import os 

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuário", max_length=30, 
                               widget=forms.TextInput(attrs={"class": "form-control input-mg", "name": "username"}))
    password = forms.CharField(label="Senha", max_length=30, 
                               widget=forms.PasswordInput(attrs={"class": "form-control input-mg", "name": "password"}))

class UserForm(forms.ModelForm):
	username = forms.CharField(label="Usuário", max_length=30, 
								widget=forms.TextInput(attrs={"class" : "form-control input-mg"}))
	email = forms.EmailField(widget=forms.TextInput(attrs={"class" : "form-control input-mg"}))
	password = forms.CharField(label="Senha", max_length=30, 
								widget=forms.PasswordInput(attrs={"class" : "form-control input-mg"}))
	confirm_password = forms.CharField(label="Confirme a senha", max_length=30, 
								widget=forms.PasswordInput(attrs={"class" : "form-control input-mg"}))

	class Meta:
		model = User
		fields = ["username", "email", "password", "confirm_password"]

class SubmitFileForm(forms.Form):
	title = forms.CharField(label="Título", 
							widget=forms.TextInput(attrs={"class" : "form-control input-mg"}))
	docfile = forms.FileField(label="Arquivo (.pdf)", 
								widget=forms.FileInput(attrs={"class" : "form-control input-mg"}))
	page = forms.CharField(label="Página", initial=1, 
								widget=forms.NumberInput(attrs={"class" : "form-control input-mg"}))
