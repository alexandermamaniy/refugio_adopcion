# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from models import Solicitud
from django.shortcuts import render
from forms import SolicitudForm
from rest_framework.views import APIView
from serializers import SolicitudSerializer
from django.http import HttpResponse
import json


# vistas basadas en clases q nos permite agregar,editar, lista y eliminar los refistros de una
#solictud de adopcion
class SolicitudList(ListView):
    model = Solicitud
    template_name = 'adopcion/solicitud_list'
    paginate_by = 3

class SolicitudCreate(CreateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'adopcion/solicitud_form.html'
    success_url = reverse_lazy('adopcion:solicitud_list')

class SolicitudUpdate(UpdateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'adopcion/solicitud_form.html'
    success_url = reverse_lazy('adopcion:solicitud_list')

class SolicitudDelete(DeleteView):
    model = Solicitud
    template_name = 'adopcion/solicitud_delete.html'
    success_url = reverse_lazy('adopcion:solicitud_list')


# vista basada en clase que obtiene un query de la tabla Solicitud, y lo serializa en formato
# Json

class SolicitudApi(APIView):
    serializer = SolicitudSerializer
    def get(self,request,format=None):
        lista = Solicitud.objects.all()
        response = self.serializer(lista,many=True)
        return HttpResponse(json.dumps(response.data),content_type='application/json')
