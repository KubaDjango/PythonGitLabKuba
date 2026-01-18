# modules for getting name of the project
from django import forms
from django.http import HttpResponse
from django.shortcuts import render

from .models import Post
#from data import gitlab_location

class MyForm(forms.Form):
    name = forms.CharField(label='NAME OF YOUR PROJECT',max_length= 100)
    location = forms.CharField(label='GITLAB GROUP LOCATION', max_length=100, initial='kuba9223326')









