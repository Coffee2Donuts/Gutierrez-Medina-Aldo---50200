from django import forms   

class RecetaForm(forms.Form):
    nombre = forms.CharField(max_length=60, required=True)
    dificultad = forms.IntegerField(min_value=1, max_value=10, required=True)
    porciones = forms.IntegerField(required=True)
    ingredientes = forms.CharField(max_length=500, required=True)
    procedimiento = forms.CharField(max_length=500, required=True)

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True, label="Cuenta de Correo")

class Chef_Form(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True, label="Cuenta de Correo")
    especialidad = forms.CharField(max_length=50, required=True)