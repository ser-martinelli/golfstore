from django.db import models

class Categoria(models.Model):

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Subcategoria(models.Model):

    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Producto(models.Model):

    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    precio = models.FloatField()
    descripcion = models.TextField()
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


