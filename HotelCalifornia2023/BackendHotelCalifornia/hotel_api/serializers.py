from rest_framework import serializers
from GestionReservas.models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    habitacionId=serializers.EmailField(required = True),
    fechaReserva=serializers.DateField(required = False),
    fechaIngreso=serializers.CharField(required = True),
    fechaEgreso=serializers.CharField(required = True),
    clienteId=serializers.IntegerField(required = True)
    class Meta:
        model = Reserva
        fields = '__all__'