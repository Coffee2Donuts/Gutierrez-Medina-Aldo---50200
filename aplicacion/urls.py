from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('home2/',home2, name="home2"),
    path('home3/',home3, name="home3"),
    path('bienvenido/', bienvenido, name="bienvenido"),
    
    path('usuario/', UsuariosList.as_view(), name="usuario"),
    path('usuario_create/', UsuarioCreate.as_view(), name="usuario_create"),
    path('usuario_edit/<int:pk>/', UsuarioEdit.as_view(), name="usuario_edit"),
    path('usuario_delete/<int:pk>/', UsuarioDelete.as_view(), name="usuario_delete"),
    path('edit_perfil/', editarPerfil, name="edit_perfil"),
    path('avatar/', agregarAvatar, name="avatar"),

    path('chefs/', chefs, name="chefs"),
    path('chef_Form/', chef_Form, name="chef_Form"),
    path('chef_actualizar/<id_chef>/', updateChef, name="chefActualizar"),
    path('chef_borrar/<id_chef>/', borrarChef, name="chefBorrar"),
    
    path('ver_recetas/', ver_recetas, name="ver_recetas"),
    path('crear_recetas/', crear_recetas, name="crear_recetas"),
    path('recetasForm/', receta_Form, name="recetasForm"),
    path('buscar/', buscar, name="buscar"),
    path('buscarRecetas/', buscarRecetas, name="buscarRecetas"),

    path('login/', login_request, name="login"),
    path('registro/', register, name="registro"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
]