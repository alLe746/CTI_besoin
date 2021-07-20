from django import forms
from django.db import models
import os

class DocumentMeta(forms.Form):
    Description = forms.CharField(label="Description", max_length=64)
    Date_demande = forms.DateField(label="Date de la Demande")


class FileUpload(forms.Form):
    file = forms.FileField(label="document Word ( .docx)")

class FileUploadjson(forms.Form):
    file = forms.FileField(label="Fichier Json ( .json, .txt,...)")

class Modeldocx(models.Model):
    docx=models.FileField()

class Jsonchoice(forms.Form):
    def __init__(self,*arguments,**kwargs):
        self.max_value = kwargs.pop('max_value')
        super().__init__(*arguments,**kwargs)
        json = forms.CharField(widget=forms.HiddenInput())
        res = forms.CharField(widget=forms.HiddenInput())
        choice = forms.IntegerField(label="valeur de I",max_value=self.max_value,min_value=0)