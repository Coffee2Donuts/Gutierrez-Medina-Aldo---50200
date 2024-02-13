from django.db import models

# Create your models here.
class V_recetas(models.Model):
    tipo = models.CharField(max_length=50)
    n_recetas = models.IntegerField()

    def __str__(self):
        return f"{self.tipo}"

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Chef(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    especialidad = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Chef"
        verbose_name_plural = "Chefs"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class C_receta(models.Model):
    Tipo = models.CharField(max_length=50)
    Ingredientes = models.IntegerField()
    Dificultad = models.IntegerField()

    def __str__(self):
        return f"{self.Tipo}"