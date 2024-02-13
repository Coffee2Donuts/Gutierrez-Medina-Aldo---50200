from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *

# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

def home2(request):
    return render(request, "aplicacion/home2.html")

def home3(request):
    return render(request, "aplicacion/home3.html")

def usuario(request):
    contexto = {'usuers': Usuario.objects.all()}
    contexto = {'chefsito': Chef.objects.all()}
    return render(request, "aplicacion/usuario.html")

def ver_recetas(request):
    contexto = {'recetass': Recetas.objects.all()}
    return render(request, "aplicacion/ver_recetas.html", contexto)

def crear_recetas(request):
    contexto = {'recetas': Recetas.objects.all()}
    return render(request, "aplicacion/crear_recetas.html", contexto)

def receta_Form(request):
    if request.method == "POST":
        miForm = RecetaForm(request.POST)
        if miForm.is_valid():
            receta_nombre = miForm.cleaned_data.get("nombre")
            receta_dificultad = miForm.cleaned_data.get("dificultad")
            receta_porciones = miForm.cleaned_data.get("porciones")
            receta_ingredientes = miForm.cleaned_data.get("ingredientes")
            receta_procedimiento = miForm.cleaned_data.get("procedimiento")
            receta = Recetas(nombre=receta_nombre, dificultad=receta_dificultad, porciones=receta_porciones, ingredientes=receta_ingredientes,
                              procedimiento=receta_procedimiento)
            
            receta.save()
            return render(request, "aplicacion/home.html")

    else:    
        miForm = RecetaForm()

    return render(request, "aplicacion/recetasForm.html", {"form": miForm })

def usuarioForm(request):
    if request.method == "POST":
        miForm = UsuarioForm(request.POST)
        if miForm.is_valid():
            usuer_nombre = miForm.cleaned_data.get("nombre")
            usuer_apellido = miForm.cleaned_data.get("apellido")
            usuer_email = miForm.cleaned_data.get("email")
            usuer = Usuario(nombre=usuer_nombre, apellido=usuer_apellido,
                                email=usuer_email,)
            usuer.save()
            return render(request, "aplicacion/home.html")

    else:    
        miForm = UsuarioForm()

    return render(request, "aplicacion/usuarioForm.html", {"form": miForm })

def chef_Form(request):
    if request.method == "POST":
        miForm = Chef_Form(request.POST)
        if miForm.is_valid():
            chef_nombre = miForm.cleaned_data.get("nombre")
            chef_apellido = miForm.cleaned_data.get("apellido")
            chef_email = miForm.cleaned_data.get("email")
            chef_especialidad = miForm.cleaned_data.get("especialidad")
            chef = Chef(nombre=chef_nombre, apellido=chef_apellido,
                                email=chef_email, especialidad=chef_especialidad)
            chef.save()
            return render(request, "aplicacion/home.html")

    else:    
        miForm = Chef_Form()

    return render(request, "aplicacion/chef_Form.html", {"form": miForm })    

def buscar(request):
    return render(request, "aplicacion/buscar.html")

def buscarRecetas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        recetas = Recetas.objects.filter(nombre__icontains=patron)
        contexto = {"receta": recetas }
        return render(request, "aplicacion/ver_recetas.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")
