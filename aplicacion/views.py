from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from django.http import HttpResponse
from .forms import *

from django.shortcuts import get_object_or_404

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms      import AuthenticationForm
from django.contrib.auth            import authenticate, login
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
#_____________________________________________________________________________________________Plantillas
def home(request):
    return render(request, "aplicacion/home.html")
@login_required
def home2(request):
    return render(request, "aplicacion/home2.html")

@login_required
def home3(request):
    return render(request, "aplicacion/home3.html")

@login_required
def bienvenido(request):
    return render(request, "aplicacion/bienvenido.html")


#______________________________________________________________________________________________Usuarios
@login_required
def usuario(request):
    return render(request, "aplicacion/usuario.html",)

class UsuariosList(LoginRequiredMixin, ListView):
    model = Usuario

class UsuarioCreate(LoginRequiredMixin, CreateView):
    model = Usuario
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('usuario')

class UsuarioEdit(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('usuario')

class UsuarioDelete(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuario')


#_______________________________________________________________________________________________Chefs
@login_required
def chefs(request):
    contexto = {'chefsito': Chef.objects.all()}
    return render(request, "aplicacion/chefs.html", contexto)

@login_required
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
            return redirect(reverse_lazy('chefs'))

    else:    
        miForm = Chef_Form()

    return render(request, "aplicacion/chef_Form.html", {"form": miForm }) 

@login_required
def updateChef(request, id_chef):
    chef = Chef.objects.get(id=id_chef)
    if request.method == "POST":
        miForm = Chef_Form(request.POST)
        if miForm.is_valid():
            chef.nombre = miForm.cleaned_data.get('nombre')
            chef.apellido = miForm.cleaned_data.get('apellido')
            chef.email = miForm.cleaned_data.get('email')
            chef.especialidad = miForm.cleaned_data.get('especialidad') 
            chef.save()
            return redirect(reverse_lazy('chefs'))   
    else:
        miForm = Chef_Form(initial={
            'nombre': chef.nombre,
            'apellido': chef.apellido,
            'email': chef.email,
            'especialidad': chef.especialidad,
        })
    return render(request, "aplicacion/chef_Form.html", {'form': miForm})

@login_required
def borrarChef(request, id_chef):
    chef = Chef.objects.get(id=id_chef)
    chef.delete()
    return redirect(reverse_lazy('chefs'))


#_______________________________________________________________________________________________Recetas
@login_required
def ver_recetas(request):
    contexto = {'recetass': Recetas.objects.all()}
    return render(request, "aplicacion/ver_recetas.html", contexto)

@login_required
def crear_recetas(request):
    contexto = {'recetas': Recetas.objects.all()}
    return render(request, "aplicacion/crear_recetas.html", contexto)

@login_required
def receta_Form(request):
    if request.method == "POST":
        miForm = RecetaForm(request.POST)
        if miForm.is_valid():
            receta_nombre = miForm.cleaned_data.get("nombre")
            receta_dificultad = miForm.cleaned_data.get("dificultad")
            receta_porciones = miForm.cleaned_data.get("porciones")
            receta_ingredientes = miForm.cleaned_data.get("ingredientes")
            receta_procedimiento = miForm.cleaned_data.get("procedimiento")
            
            # Obtener el usuario actualmente logueado
            usuario = request.user

            # Guardar la receta como 'creada' por el usuario logueado
            receta = Recetas(nombre=receta_nombre, dificultad=receta_dificultad, porciones=receta_porciones, 
                             ingredientes=receta_ingredientes, procedimiento=receta_procedimiento,
                             usuario=usuario)
            
            receta.save()
            return render(request, "aplicacion/home.html")

    else:    
        miForm = RecetaForm()

    return render(request, "aplicacion/recetasForm.html", {"form": miForm })


@login_required
def mostrar_receta(request, receta_id):
    receta = get_object_or_404(Recetas, id=receta_id)

    # Mostrar los ingredientes y procedimiento en formato de lista
    ingredientes_lista = receta.ingredientes.split('\n')
    procedimiento_lista = receta.procedimiento.split('\n')

    return render(request, "aplicacion/mostrar_receta.html", {
        'receta': receta,
        'ingredientes_lista': ingredientes_lista,
        'procedimiento_lista': procedimiento_lista
    })

@login_required
def buscar(request):
    return render(request, "aplicacion/buscar.html")

@login_required
def buscarRecetas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        find = Recetas.objects.filter(nombre__icontains=patron)
        contexto = {"recetass": find }
        return render(request, "aplicacion/ver_recetas.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")


#_______________________________________________________________________________________________Login, Logout, Registro
def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)
        #___________________________________________________________ Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            return render(request, "aplicacion/bienvenido.html")
        
        #___________________________________________________________
        else:
            return redirect(reverse_lazy('login'))
        
    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm })    

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("usuername")
            miForm.save()
            return redirect(reverse_lazy('login'))

    else:    
        miForm = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": miForm })  

#_______________________________________________________________________________________________Editar perfil de usuario
@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            user.save()
            return render(request, "aplicacion/home.html")
    else:    
        form = UserEditForm(instance=usuario)

    return render(request, "aplicacion/edit_perfil.html", {"form": form })

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)

            # ________________________________________________Eliminar el avatar antigüo
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            
            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # __________________________________________________url de la imagen en request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "aplicacion/bienvenido.html")

    else:    
        form = AvatarForm()

    return render(request, "aplicacion/avatar.html", {"form": form }) 