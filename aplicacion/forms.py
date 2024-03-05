from django import forms   
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Recetas

#class RecetaForm(forms.Form):
    #nombre = forms.CharField(max_length=60, required=True)
    #dificultad = forms.IntegerField(min_value=1, max_value=10, required=True)
    #porciones = forms.IntegerField(required=True)
    #ingredientes = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows':5, 'cols':50 }), required=True)
    #procedimiento = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows':5, 'cols':50 }), required=True)

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Recetas
        fields = ['nombre', 'dificultad', 'porciones', 'ingredientes', 'procedimiento', 'imagen']
        widgets = {
            'ingredientes': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
            'procedimiento': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
        }

    def __init__(self, *args, **kwargs):
        super(RecetaForm, self).__init__(*args, **kwargs)
        self.fields['imagen'].required = False

class RecetaEditForm(UserCreationForm):
    nombre = forms.CharField(max_length=60, required=False)
    dificultad = forms.IntegerField(min_value=1, max_value=10, required=False)
    porciones = forms.IntegerField(required=False)
    ingredientes = forms.CharField(label="Ingredientes", max_length=500, widget=forms.Textarea(attrs={'rows':5, 'cols':50 }), required=False)
    procedimiento = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows':5, 'cols':50 }), required=False)
    class Meta:
        model = Recetas
        fields = ['nombre', 'dificultad', 'porciones', 'ingredientes', 'procedimiento', 'imagen']
    

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True, label="Cuenta de Correo")

class Chef_Form(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True, label="Cuenta de Correo")
    especialidad = forms.CharField(max_length=50, required=True)

class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre/s (opcional)", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido/s (opcional)", max_length=50, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserEditForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre/s (opcional)", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido/s (opcional)", max_length=50, required=False)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)