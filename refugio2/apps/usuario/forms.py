from django.contrib.auth.forms import UserCreationForm
from models import Usuario
from django import forms
from django.contrib.auth.models import User
"""en este modulo presentamos los formulario que vamos a utilizar para agregar datos a nuestra BD"""

# formulario para el modelo User que esta relacionado con el formulario Usuario
class UserForm(UserCreationForm):

    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}), )

    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        strip=False, )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

        labels = {
            'username':'Nombre de usuario',
            'first_name':'Nombre',
            'last_name':'Apellidos',
            'email':'Correo',
        }
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }


# formulario para el modelo Usuario
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'edad',
            'telefono',
            'domicilio',
        ]

        labels = {
            'edad':'Edad',
            'telefono':'Telefono',
            'domicilio':'Domicilio',
        }

        widgets = {
            'edad':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'docimilio':forms.Textarea(attrs={'class':'form-control'}),
        }

