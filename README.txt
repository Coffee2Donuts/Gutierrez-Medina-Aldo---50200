<<<<<<< HEAD
# Nombre de Proyecto: Sabores en Red
# Alumno: Aldo Gutierrez Medina
# Fecha: 8/3/24
# Version: 4.9
=======
Proyecto de Gutierrez Medina Aldo
>>>>>>> a1364510abd130f64171fa99f6934fe67664a8ff

Pagina web para ver, crear, editar y comentar recetas de comida

Usuario admin:
Kouhi
coder.login

<<<<<<< HEAD
Casos de pruebas: https://1drv.ms/x/s!AkwI7NLlrfMtl0bS8rzSfxwfv8d7?e=b0mzIu
Video de expliación: 

=======
=======

Usuario admin:
Kouhi
coder.login


>>>>>>> a1364510abd130f64171fa99f6934fe67664a8ff
Contiene:

-Clases en modelos:
    Recetas: Guarda todo lo relacionado a las recetas, formularios, edición, listas o tablas, search, etc.
    
    
    Usuarios: (Utiliza los usuarios de Django) Se utilizan para guardar las recetas en sus respectivos usuarios, 
        también se pueden buscar los usuarios y ver las recetas creadas por estos
    
    
    Avatar: Cambia el avatar de los usuarios, y muestra uno por default
    
    
    Comentarios: Crear, guardar y mostrar comentarios en las recetas, 
        muestra la fecha en la que se hizo el comentario

-Formulario para:
    Login
    Crear Recetas
    Editar recetas
    Registro de usuario nuevo
    Cambiar avatar
    Editar usuario
    Buscar recetas
    Buscar usuarios
    Hacer comentarios en las recetas

- Pagina de inicio de sesión cerrada o no iniciada o no registrado (no permite entrar a las demás urls si no estas logueado)

- Pagina de inicio para usuarios logueados y barra de menú:
    Inicio
    Ver Recetas
    Mis Recetas
    Usuarios
    Perfíl
    Acerca de mí
    Avatar, y usuario
    Logout

-Las aplicaciones heredan templates de home.html home2.html y home3.html

<<<<<<< HEAD
=======
=======

-Error no resuelto:
!!!El logout no me funciona de ninguna manera.!!!

Siempre me aparece lo siguiente:

Method Not Allowed (GET): /aplicacion/logout/
Method Not Allowed: /aplicacion/logout/

Investigue el problema y encontré de debería cambiarlo al método POST lo cual quedaría en el logout.html así:

______________________________________
{% extends ‘aplicacion/home.html’ %}

{% block logout %}

{% csrf_token %}
    <form action\=”” method\=“post”>
    {% csrf_token %}

    <button type\=“submit”>Logout</button>

    </form>

{% endblock logout %}
_________________________________________

La urls la intente poner de dos maneras:

from django.contrib.auth.views import LogoutView
path(‘logout/’, LogoutView.as_view(template_name=“aplicacion/logout.html”), name=“logout”),

y

from django.contrib.auth import views as auth_views
path(‘logout/’, auth_views.LogoutView.as_view(), name\=‘logout’),

También agregué lo siguiente a settings.py

# URL de redireccionamiento después del logout
LOGOUT_REDIRECT_URL = ‘/aplicacion/’

Nada de lo anterior me funcionó 

También hay un error con mostrar el avatar default:
Not Found: /media/avatares/default.png
Not Found: /aplicacion/ver_recetas/js/scripts.js


>>>>>>> a1364510abd130f64171fa99f6934fe67664a8ff
