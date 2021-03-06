# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from models import File
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
		fields = ["username", "email", "password"]

class UserEditForm(forms.ModelForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={"class" : "form-control input-mg"}))
	password = forms.CharField(label="Nova senha", max_length=30, required=False,
								widget=forms.PasswordInput(attrs={"class" : "form-control input-mg"}))
	confirm_password = forms.CharField(label="Confirme a nova senha", max_length=30, required=False,
								widget=forms.PasswordInput(attrs={"class" : "form-control input-mg"}))

	class Meta:
		model = User
		fields = ["email"]

class SubmitFileForm(forms.Form):
	title = forms.CharField(label="Título",
							widget=forms.TextInput(attrs={"class" : "form-control input-mg",
														  "maxlength": "100"}))
	docfile = forms.FileField(label="Arquivo (.pdf ou .txt)",
							widget=forms.FileInput(attrs={"class" : "form-control input-mg"}))
	is_summarized = forms.BooleanField(label="Sumarizado", required=False,
							widget=forms.CheckboxInput(attrs={
								"data-toggle" : "toggle",
								"data-onstyle" : "default",
								"data-on" : "Sim",
								"data-off" : "Não"
								}))
	starts_at = forms.DecimalField(label="Início", min_value=0, required=False,
							widget=forms.NumberInput(attrs={
								"class" : "form-control"
								}))
	ends_at = forms.DecimalField(label="Fim", required=False, min_value=0,
							widget=forms.NumberInput(attrs={
								"class" : "form-control"
								}))
