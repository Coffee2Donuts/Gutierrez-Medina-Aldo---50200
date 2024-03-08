from django.urls import path, include
from .views import *
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #Plantillas
    path('', home, name="home"),
    path('home2/',home2, name="home2"),
    path('home3/',home3, name="home3"),
    path('bienvenido/', bienvenido, name="bienvenido"),
    
    #urls relacionadas con los usuarios
    path('usuarios/', views.usuario_list, name='usuario_list'),
    path('usuarios/<int:usuario_id>/recetas/', views.ver_recetas_usuario, name='ver_recetas_usuario'),
    path('edit_perfil/', editarPerfil, name="edit_perfil"),
    path('avatar/', agregarAvatar, name="avatar"),
    path('buscarUsuarios/', buscarUsuarios, name="buscarUsuarios"),
    
    #urls relacionadas con recetas
    path('ver_recetas/', views.ver_recetas, name='ver_recetas'),
    path('mis_recetas/', views.mis_recetas, name='mis_recetas'),
    path('recetas_form/', receta_Form, name="recetas_form"),
    path('buscar/', buscar, name="buscar"),
    path('buscarRecetas/', buscarRecetas, name="buscarRecetas"),
    path('mostrar_receta/<int:receta_id>/', views.mostrar_receta, name='mostrar_receta'),
    path('receta_edit/<int:pk>/', RecetaEdit.as_view(), name="receta_edit"),
    path('receta_delete/<int:pk>/', RecetaDelete.as_view(), name="receta_delete"),
    path('receta/<int:receta_id>/', views.mostrar_receta, name='mostrar_receta'),


    # URLs relacionadas con los comentarios
    path('agregar_comentario/<int:receta_id>/', views.agregar_comentario, name='agregar_comentario'),

    #urls de login, registro de nuevo usuario y logout
    path('login/', login_request, name="login"),
    path('registro/', register, name="registro"),
    path('logout/', views.logout_usuario, name='logout'),
    #path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"), (esta versión de logout no funcionó)

    #Acerca de mí
    path('about_me/', aboutME, name="about_me"),
    
    
    #urls relacionadas con chefs (no se utilizan a partir de la version 4.0 del proyecto)
    path('chefs/', chefs, name="chefs"),
    path('chef_Form/', chef_Form, name="chef_Form"),
    path('chef_actualizar/<id_chef>/', updateChef, name="chefActualizar"),
    path('chef_borrar/<id_chef>/', borrarChef, name="chefBorrar"),

]