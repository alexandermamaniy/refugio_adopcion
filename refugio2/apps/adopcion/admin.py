# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Solicitud

#agregammos el modelo Solicitud para q un super usuario pueda hacer cambios a la BD
admin.site.register(Solicitud)