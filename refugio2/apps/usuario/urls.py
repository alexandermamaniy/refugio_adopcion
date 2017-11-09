from django.conf.urls import url,include
from django.contrib import admin
from views import RegistroUsuario
from django.http import HttpResponse

# nombre con el cual podemos referirnos hacia las URL de esta app
app_name = 'usuario'

# url para el registro de Usuario
urlpatterns = [
    url(r'^registrar/$',RegistroUsuario.as_view(),name='registrar'),
]
