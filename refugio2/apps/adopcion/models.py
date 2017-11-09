# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..usuario.models import Usuario

"""este archivo almacena todo los modelos para la app adopcion"""


# modelo Solicitud que tiene una relacion uno a Muchos con el modelo Usuarios
# este almacenas las solicitudes para adoptar a una mascota

class Solicitud(models.Model):
    usuario = models.ForeignKey(Usuario,null=True,blank=True)
    numero_mascotas = models.IntegerField()
    razones = models.TextField()
    def __str__(self):
        return '{}'.format(self.usuario.user.first_name)
