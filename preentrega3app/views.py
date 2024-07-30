from django.shortcuts import render,redirect 
from preentrega3app.models import Autor, Libro, Genero
from preentrega3app.forms import AutorForm

def inicio(request):
    return render(request, "preentrega3app/index.html")

#Formulario para agregar nuevos autores
def formulario_autor(request):
    if request.method == "POST":
        nuevo_autor = Autor(nombre = request.POST["nombre"], bio = request.POST["bio"])
        nuevo_autor.save()

        return render (request, "preentrega3app/index.html")
    return render(request,"preentrega3app/formulario_autor.html")

#Formulario para agregar nuevos libros
def formulario_libro(request):
    if request.method == "POST":
        nuevo_libro = Libro(titulo = request.POST["titulo"], fecha = request.POST["fecha"])
        nuevo_libro.save()

        return render (request, "preentrega3app/index.html")
    return render(request,"preentrega3app/formulario_libro.html")

#Formulario para agregar generos
def formulario_genero(request):
    if request.method == "POST":
        nuevo_genero = Genero(tipo = request.POST["tipo"], descripcion = request.POST["descripcion"])
        nuevo_genero.save()

        return render (request, "preentrega3app/index.html")
    return render(request,"preentrega3app/formulario_genero.html")

#Busqueda de autor
def busqueda_autor(request):
    if request.method == "POST":

        mi_formulario = AutorForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            autor = Autor.objects.filter(nombre__icontains=informacion["nombre"])
            return render(request, "preentrega3app/mostrar_autores.html", {"autor":autor})
    else:
        mi_formulario = AutorForm()
    
    return render(request, "preentrega3app/busqueda_autor.html",{"mi_formulario":mi_formulario})

