from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    #autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return self.titulo

class Genero(models.Model):
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo
