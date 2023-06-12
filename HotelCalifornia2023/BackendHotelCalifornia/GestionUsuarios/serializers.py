from rest_framework.serializers import ModelSerializer
from GestionUsuarios.models import Cliente

class ClientesSerializer(ModelSerializer):
   class Meta:
        model = Cliente
        fields = ('clienteId', 'nombre', 'apellido', 'password', 'usuario', 'fechaDeNacimiento')

   