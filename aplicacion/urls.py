from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('home2/',home2, name="home2"),
    path('home3/',home3, name="home3"),
    
    path('usuario/', usuario, name="usuario"),
    path('usuarioForm/', usuarioForm, name="usuarioForm"),
    path('see_usuarios/', see_usuarios, name="see_usuarios"),

    path('chefs/', chefs, name="chefs"),
    path('chef_Form/', chef_Form, name="chef_Form"),
    path('see_chefs/', see_chefs, name="see_chefs"),
    path('chef_actualizar/<id_chef>/', updateChef, name="chefActualizar"),
    path('chef_borrar/<id_chef>/', borrarChef, name="chefBorrar"),
    
    path('ver_recetas/', ver_recetas, name="ver_recetas"),
    path('crear_recetas/', crear_recetas, name="crear_recetas"),
    path('recetasForm/', receta_Form, name="recetasForm"),
    path('buscar/', buscar, name="buscar"),
    path('buscarRecetas/', buscarRecetas, name="buscarRecetas"),

    
]