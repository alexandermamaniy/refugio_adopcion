# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Usuario

#agregammos el modelo usuario para que un super usuario pueda hacer cambios a la BD
admin.site.register(Usuario)


