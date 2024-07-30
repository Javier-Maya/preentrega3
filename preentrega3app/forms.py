from django import forms
from .models import Autor, Libro, Genero

class AutorForm(forms.Form):
    nombre = forms.CharField()
