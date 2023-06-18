from rest_framework import serializers
from GestionReservas.models import Reserva
from Facturacion.models import Factura, Detalle, DetallePago

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'

class DetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle
        fields = '__all__'

class DetallePagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePago
        fields = '__all__'