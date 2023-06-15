from rest_framework import serializers
from GestionUsuarios.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    imagen=serializers.CharField(required=False),
    nombre=serializers.CharField(required = True),
    apellido=serializers.CharField(required = True),
    usuario=serializers.EmailField(required = True),
    password=serializers.CharField(required = True),
    fechaDeNacimiento=serializers.DateField(required = True),
    telefono=serializers.CharField(required = True)
    ciudad=serializers.CharField(required = True)
    class Meta:
        model = Cliente
        fields = '__all__'
