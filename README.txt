Tercera pre-entrega Gutierrez Medina Aldo

Pagina web para ver y compartir recetas

http://localhost:8000/aplicacion/ 
http://localhost:8000/aplicacion/ver_recetas/
http://localhost:8000/aplicacion/crear_recetas/
http://localhost:8000/aplicacion/usuario/
<<<<<<< HEAD
http://127.0.0.1:8000/aplicacion/recetasForm/
http://127.0.0.1:8000/aplicacion/usuarioForm/
http://127.0.0.1:8000/aplicacion/chef_Form/
http://127.0.0.1:8000/aplicacion/see_usuarios/
http://127.0.0.1:8000/aplicacion/see_chefs/
http://127.0.0.1:8000/aplicacion/buscar/
y más

Contiene:

-Clases en modelos:
    Recetas
    Usuario
    Chef
    Avatar

-Formulario para:
    Crear Recetas
    Login
    Registro
    Cambiar avatar
    Editar usuario
    Editar Chef
    Editar Perfil


-Formulario para buscar recetas en la base de datos
    http://127.0.0.1:8000/aplicacion/buscar/

-Las aplicaciones heredan templates de home.html home2.html y home3.html


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


