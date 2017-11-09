# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Vacuna,Mascota

#agregammos el modelo Vacuna y Mascota para q un super usuario pueda hacer cambios a la BD
admin.site.register(Vacuna)
admin.site.register(Mascota)

# Register your models here.
