from rest_framework.serializers import ModelSerializer
from models import Solicitud


"""este archivo contiene el Serializer del modelo Solicitud, para fines comerciales"""

# este serializer nos muestra el usuarios,nro_mascotas y las razones por la cual quiere adoptar

class SolicitudSerializer(ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ('usuario','numero_mascotas','razones')
