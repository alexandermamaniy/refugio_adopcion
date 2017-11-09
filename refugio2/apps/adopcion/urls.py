from django.conf.urls import url,include
from views import SolicitudList,SolicitudUpdate,SolicitudCreate,SolicitudDelete,SolicitudApi
from django.contrib.auth.decorators import login_required
app_name='adopcion'

urlpatterns = [
                #URL que nos permite  ver los template para agregar,editar, listar y eliminar solicitudes
            url(r'solicitud_list',login_required(SolicitudList.as_view()),name='solicitud_list'),
            url(r'solicitud_create',login_required(SolicitudCreate.as_view()),name='solicitud_create'),
            url(r'solicitud_update/(?P<pk>\d+)/',login_required(SolicitudUpdate.as_view()),name='solicitud_update'),
            url(r'solicitud_delete/(?P<pk>\d+)/',login_required(SolicitudDelete.as_view()),name='solicitud_delete'),

            #URL que nos muestra el serializer del modelo Solicitud
            url(r'solicitud_api/$',SolicitudApi.as_view(),name='solicitud_api'),

]
