from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('usuario/', usuario, name="usuario"),
    path('ver_recetas/', ver_recetas, name="ver_recetas"),
    path('crear_recetas/', crear_recetas, name="crear_recetas"),
    path('home2/',home2, name="home2"),
    path('home3/',home3, name="home3"),
        
    path('recetasForm/', receta_Form, name="recetasForm"),
    path('usuarioForm/', usuarioForm, name="usuarioForm"),
    path('chef_Form/', chef_Form, name="chef_Form"),
    
    path('buscar/', buscar, name="buscar"),
    path('buscarRecetas/', buscarRecetas, name="buscarRecetas"),

    
]