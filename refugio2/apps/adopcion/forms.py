from django import forms
from models import Solicitud


"""esta archivo contiene el formulario de nuetro modelo Adopcion"""


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud

        fields = [
            'usuario',
            'numero_mascotas',
            'razones'
        ]

        labels = {
            'usuario':'Usuario',
            'numero_mascotas':'Numero Mascotas',
            'razones':'Razones',
        }

        widgets = {
            'usuario':forms.Select(attrs={'class':'form-control'}),
            'numero_mascotas':forms.TextInput(attrs={'class':'form-control'}),
            'razones': forms.TextInput(attrs={'class':'form-control'}),
        }