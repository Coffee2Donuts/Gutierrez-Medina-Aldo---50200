from django import forms   
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RecetaForm(forms.Form):
    nombre = forms.CharField(max_length=60, required=True)
    dificultad = forms.IntegerField(min_value=1, max_value=10, required=True)
    porciones = forms.IntegerField(required=True)
    ingredientes = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows':5, 'cols':50 }), required=True)
    procedimiento = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows':5, 'cols':50 }), required=True)

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