from django.urls import path
from preentrega3app import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("formulario_autor", views.formulario_autor, name="formulario_autor"),
    path("formulario_libro", views.formulario_libro, name="formulario_libro"),
    path("formulario_genero", views.formulario_genero, name="formulario_genero"),
    path("busqueda_autor", views.busqueda_autor, name="busqueda_autor"),
]
