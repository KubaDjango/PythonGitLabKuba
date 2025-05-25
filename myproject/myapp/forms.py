# modules for getting name of the project
from django import forms
from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


class MyForm(forms.Form):
    name = forms.CharField(label='NAME OF YOUR PROJECT',max_length= 100)
    location = forms.CharField(label='GITLAB GROUP LOCATION', max_length=100, initial='kuba474650')










#
#
#
# ################
# class LinearEquationForm(forms.Form):
#     a = forms.FloatField(label="Współczynnik a")
#     b = forms.FloatField(label="Współczynnik b")
#
#
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ["title", "content"]
#         labels = {"title": "Tytuł posta", "content": "Treść posta"}
#
#
# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ["title", "image"]
#         labels = {"title": "Tytuł obrazka", "image": "Obrazek"}
#
#     def clean_image(self):
#         image = self.cleaned_data.get('image')
#         if image:
#             if not image.name.lower().endswith('.jpg'):
#                 raise forms.ValidationError("Tylko pliki JGP są dozwolone!")
#         return image