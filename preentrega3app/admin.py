from django.contrib import admin
from .models import Autor, Libro, Genero

# Register your models here.
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Genero)