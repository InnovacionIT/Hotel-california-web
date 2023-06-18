from rest_framework import serializers
from GestionReservas.models import Reserva
from .models import Servicio

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['servicioId', 'servicio']


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'