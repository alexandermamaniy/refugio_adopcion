from rest_framework.serializers import ModelSerializer
from models import Mascota,Vacuna

"""este archivo contiene el Serializer de los modelos Mascotas y Vacunas, para fines comerciales"""

# este serializer nos muestra el nombre,sexo,edad y usuario de la mascota
class MascotaSeriaizer(ModelSerializer):
    class Meta:
        model = Mascota
        fields = ('nombre','sexo','edad_aproximada','usuario')

# este serializer nos muestra las vacunas con que cuenta el refugio
class VacunaSerializer(ModelSerializer):
    class Meta:
        model = Vacuna
        fields = ('id','nombre')

