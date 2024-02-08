from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('usuario/', usuario, name="usuario"),
    path('ver_recetas/', ver_recetas, name="ver_recetas"),
    path('crear_recetas/', crear_recetas, name="crear_recetas"),

    
]