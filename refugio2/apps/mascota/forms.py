from django import forms
from models import Mascota, Vacuna

"""esta archivo contiene el formulario de nuetro modelo Mascota"""

class MascotaForm(forms.ModelForm):
    class Meta:
        model=Mascota

        fields = [
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'usuario',
            'vacuna',
        ]
        labels = {
            'nombre':'Nombre',
            'sexo':'Sexo',
            'edad_aproximada':'Edad Aproximada',
            'fecha_rescate':'Fecha de rescate',
            'usuario':'Adoptante',
            'vacuna':'Vacuna',
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'sexo':forms.TextInput(attrs={'class':'form-control'}),
            'edad_aproximada':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate':forms.TextInput(attrs={'class':'form-control'}),
            'usuario':forms.Select(attrs={'class':'form-control'}),
            'vacuna':forms.CheckboxSelectMultiple(),
        }

