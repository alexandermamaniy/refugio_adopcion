from django.conf.urls import url,include
from views import MascotaList,MascotaCreate,MascotaUpdate,MascotaDelete
from django.contrib.auth.decorators import login_required
from views import VacunaApi,MascotaApi
app_name = 'mascota'

urlpatterns = [
    #URL que nos permite crear,editas,listar y eliminar el registro de una mascota
    url(r'^list/$',login_required(MascotaList.as_view()),name='mascota_list'),
    url(r'^create/$',login_required(MascotaCreate.as_view()),name='mascota_create'),
    url(r'^update/(?P<pk>\d+)/',login_required(MascotaUpdate.as_view()),name='mascota_update'),
    url(r'^delete/(?P<pk>\d+)/$',login_required(MascotaDelete.as_view()),name='mascota_delete'),

    #URLs que nos muestra los serializer
    url(r'^mascota_api/$',MascotaApi.as_view(),name='mascota_api'),
    url(r'^vacuna_api/$',VacunaApi.as_view(),name='vacuna_api'),


]
