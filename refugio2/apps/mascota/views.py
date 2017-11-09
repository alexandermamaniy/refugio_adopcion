# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from models import Mascota, Vacuna
from forms import MascotaForm
from rest_framework.views import APIView
from serializers import MascotaSeriaizer,VacunaSerializer
from django.http import HttpResponse
import json

# vista para el home
def home(request):
    return render(request,'home.html')

# vista basada en clases que lista las mascotas de la BD
class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'
    paginate_by = 3

# vista basada en clases que aniade una mascota a la BD
class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_list')

# vista basada en clase que acualiza los datos de una mascota y los vuele a guardar a la BD
class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_list')

# vista basade en clase que elimina un registro de una mascota
class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('mascota:mascota_list')


#vista basade en clase que nos muestra los datos del serializer del modelo Mascota
class MascotaApi(APIView):
    serializer = MascotaSeriaizer
    def get(self,request,format=None):
        lista = Mascota.objects.all()
        response = self.serializer(lista,many=True)
        return HttpResponse(json.dumps(response.data),content_type='application/json')

# vista basada en clase q nos muestra el serializer del modelo Vacuna
class VacunaApi(APIView):
    serializer = VacunaSerializer
    def get(self,request,format=None):
        lista = Vacuna.objects.all()
        response = self.serializer(lista,many=True)
        return HttpResponse(json.dumps(response.data),content_type = 'application/json')

