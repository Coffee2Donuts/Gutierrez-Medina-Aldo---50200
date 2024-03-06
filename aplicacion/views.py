from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from django.http import HttpResponse
from .forms import *

from django.shortcuts import get_object_or_404, redirect

from django.core.exceptions import ObjectDoesNotExist

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth            import logout
from django.contrib.auth.forms      import AuthenticationForm
from django.contrib.auth            import authenticate, login
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models               import Count


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

def usuario_list(request):
    usuarios = User.objects.annotate(num_recetas=Count('recetas')).all()
    return render(request, 'aplicacion/usuario_list.html', {'usuarios': usuarios})

def ver_recetas_usuario(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    recetas_usuario = Recetas.objects.filter(usuario=usuario)
    return render(request, 'aplicacion/ver_recetas_usuario.html', {'usuario': usuario, 'recetas_usuario': recetas_usuario})

@login_required
def buscarUsuarios(request):
    if 'buscar' in request.GET:
        patron = request.GET["buscar"]
        usuarios = User.objects.filter(username__icontains=patron).annotate(num_recetas=Count('recetas'))
        contexto = {"usuarios": usuarios}
        return render(request, "aplicacion/usuario_list.html", contexto)
    return HttpResponse("No se ingresaron patrones de búsqueda")


#_______________________________________________________________________________________________Recetas
@login_required
def ver_recetas(request):
    contexto = {'recetass': Recetas.objects.all()}
    return render(request, "aplicacion/ver_recetas.html", contexto)

@login_required
def mis_recetas(request):
    # Filtra las recetas del usuario logueado
    recetass = Recetas.objects.filter(usuario=request.user)
    contexto = {'recetass': recetass}
    return render(request, "aplicacion/mis_recetas.html", contexto)

@login_required
def receta_Form(request):
    #Formulario para crear recetas
    if request.method == "POST":
        mi_form = RecetaForm(request.POST, request.FILES)
        if mi_form.is_valid():
            receta = mi_form.save(commit=False)
            receta.usuario = request.user
            receta.save()
            return redirect("ver_recetas")
    else:
        mi_form = RecetaForm()
    
    return render(request, "aplicacion/recetas_form.html", {"form": mi_form })

class RecetaEdit(LoginRequiredMixin, UpdateView):
    model = Recetas
    form_class = RecetaForm
    success_url = reverse_lazy('mis_recetas')
    template_name = 'aplicacion/receta_edit.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()  # Pasar la instancia de la receta al formulario
        return kwargs

class RecetaDelete(LoginRequiredMixin, DeleteView):
    model = Recetas
    success_url = reverse_lazy('mis_recetas')

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

def agregar_comentario(request, receta_id):
    receta = get_object_or_404(Recetas, id=receta_id)
    
    if request.method == 'POST':
        texto = request.POST.get('texto')
        try:
            avatar = Avatar.objects.get(user=request.user)
        except Avatar.DoesNotExist:
            avatar = None  # Si no hay avatar, asignamos None
        
        comentario = Comentario(usuario=request.user, receta=receta, texto=texto, avatar=avatar)
        comentario.save()
        return redirect('mostrar_receta', receta_id=receta_id)

    return render(request, 'aplicacion/agregar_comentario.html', {'receta': receta})


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
        usuario = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)
            try:
                avatar = Avatar.objects.get(user=user).imagen.url
            except ObjectDoesNotExist:
                avatar = "/media/avatares/default.png"
            request.session["avatar"] = avatar
            return render(request, "aplicacion/bienvenido.html")
        else:
            return redirect(reverse_lazy('login'))
    miForm = AuthenticationForm()
    return render(request, "aplicacion/login.html", {"form": miForm }) 

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            miForm.save()
            return redirect(reverse_lazy('login'))
    else:    
        miForm = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": miForm })  

def logout_usuario(request):
    logout(request)
    return redirect("home")

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

            # ___________________________________________________________________Eliminar el avatar antigüo
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            
            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ____________________________________________________________________url de la imagen en request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "aplicacion/bienvenido.html")

    else:    
        form = AvatarForm()

    return render(request, "aplicacion/avatar.html", {"form": form }) 


#_______________________________________________________________________________________________Chefs

#Estas funciones ya no se utilizaron a partir de la version 4.0 del proyecto pero si funcionan

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