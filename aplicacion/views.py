from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

def usuario(request):
    return render(request, "aplicacion/usuario.html")

def ver_recetas(request):
    contexto = {'recetas': V_recetas.objects.all()}
    return render(request, "aplicacion/ver_recetas.html", contexto)


def crear_recetas(request):
    return render(request, "aplicacion/crear_recetas.html")
