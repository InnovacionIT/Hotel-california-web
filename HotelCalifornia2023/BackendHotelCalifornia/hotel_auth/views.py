from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .serializer import ClienteSerializer
from rest_framework.authtoken.models import Token

class LoginView(APIView):
    def post(self, request):  # METODO POST QUE OBTIENE EL USUARIO Y CONTRASEÑA DE LOS DATOS ENVIADOS EN LA SOLICITUD.
        usuario = request.data.get('usuario')
        password = request.data.get('password')

        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)

            if user.is_superuser:
                token, _ = Token.objects.get_or_create(user=user) # Crea el token
                return Response({'token de admin': token.key})  # Devuelve token de sesion como administrador
            else:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token de usuario': token.key})
        else:
            return Response({'error': 'Credenciales Invalidas'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        logout(request)

        return Response(status=status.HTTP_200_OK)
    
class SingupView(generics.CreateAPIView):
    serializer_class = ClienteSerializer