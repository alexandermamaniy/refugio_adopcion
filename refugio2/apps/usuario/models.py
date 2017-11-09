# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# modelo que es el que almacena los datos de cada usuario, que esta relacionado con el modelo
# User que nos ofrece Django para loguearnos y delosguearnos

class Usuario(models.Model):
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    domicilio = models.TextField()
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return "{} {}".format(self.user.first_name,self.user.last_name)