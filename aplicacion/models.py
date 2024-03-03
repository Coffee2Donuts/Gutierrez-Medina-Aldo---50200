from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Recetas(models.Model):
    nombre = models.CharField(max_length=60)
    dificultad = models.IntegerField()
    porciones = models.IntegerField()
    ingredientes = models.CharField(max_length=500)
    procedimiento = models.CharField(max_length=500)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.nombre}"
    

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

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
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}" 
