from GestionUsuarios.models import Cliente
from GestionUsuarios.serializers import ClientesSerializer
from rest_framework import generics

from django.shortcuts import render

class ClienteCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer

class ClienteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer
