# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from forms import UserForm,UsuarioForm
from models import Usuario

"""En este archivo presentamos las vistas para cada Template y URL"""

#vista basada en clase que añade un nuevo usuario a nuetra BD
#esta Vista la modificamos para q pueda enviar 2 formularios, ya q esta trabajando con el modelo
#Usuario que esta relacionado con el modelo User
class RegistroUsuario(CreateView):
    model = Usuario
    template_name = 'usuario/registrar.html'
    form_class = UsuarioForm
    second_form_class = UserForm
    success_url = reverse_lazy('login')
    # sobre escribimos el metodo que envia el formulario al template
    def get_context_data(self,**kwargs):
        context = super(RegistroUsuario, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)

        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context



    # sobre escribimos el metodo post que es el que guarda los  datos en la BD , y ademas Valida
    # los datos, en caso de no ser valido, le vuelve a mandar al template
    def post(self,request,*args,**kwargs):
        self.object=self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.user = form2.save()
            solicitud.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form,form2=form2))



