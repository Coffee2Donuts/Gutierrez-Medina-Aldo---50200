# Nombre de Proyecto: Sabores en Red
# Alumno: Aldo Gutierrez Medina
# Fecha: 8/3/24
# Version: 4.9

Pagina web para ver, crear, editar y comentar recetas de comida

Usuario admin:
Kouhi
coder.login

Casos de pruebas: https://1drv.ms/x/s!AkwI7NLlrfMtl0bS8rzSfxwfv8d7?e=b0mzIu
Video de expliación: https://drive.google.com/file/d/1OhXgayIGUtu_1Bh6dfObawp81Tz_Norz/view?usp=drive_link

=======
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

=======
