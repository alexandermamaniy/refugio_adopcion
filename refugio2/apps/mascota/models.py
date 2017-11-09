# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..usuario.models import Usuario

"""este archivo almacena todo los modelos para la app Mascota"""


# modelo Vacuna que tiene una relacion Muchos a Muchos con el modelo Mascota
#ojo todos los modelos extienden del la clase      models.Model
class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

# Modelo Mascota q esta relacionado con el modelo Vacuna y modelo Usuario
class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()  # estamos definiendo a un tipo de dato entero
    fecha_rescate = models.DateField()  # estamos definiendo un tipo de dato DATE
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)

