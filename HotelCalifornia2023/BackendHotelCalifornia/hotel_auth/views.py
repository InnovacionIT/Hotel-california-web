from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.db.models import Q
from django.contrib import messages
from .serializer import ClienteSerializer, LoginSerializer
from GestionUsuarios.models import Cliente

# User = get_user_model()

class LoginView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    def post(self, request):  
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)

        return Response(ClienteSerializer(user).data, status=status.HTTP_200_OK)
        # usuario = request.data.get('usuario')
        # password = request.data.get('password')

        # # user = User.objects.filter(Q(usuario=usuario)).first()

        # user = authenticate(request, usuario=usuario, password=password)
        # if user is not None:
        #     # if user.check_password(password):
        #         login(request, user)
        #         return Response(ClienteSerializer(user).data, status=status.HTTP_200_OK)
        
        # return Response(status=status.HTTP_404_NOT_FOUND)
        #         if user.is_superuser:
        #             token, _ = Token.objects.get_or_create(user=user) # Crea el token
        #             return Response({'token de admin': token.key})  # Devuelve token de sesion como administrador
        #         else:
        #             token, _ = Token.objects.get_or_create(user=user)
        #             return Response({'token de usuario': token.key})
        #     else:
        #         # serializer = self.get_serializer(data=request.data)
        #         # if serializer.is_valid():
        #         #     self.perform_authentication(serializer)
        #         #     token, _ = Token.objects.get_or_create(user=user)
        #         #     return Response({'token de usuario': token.key})
        #         # else:
        #             return Response({'error': 'Credenciales Invalidas'}, status=status.HTTP_401_UNAUTHORIZED)
        # else:
        #     return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

class LogoutView(APIView):
    permission_classes= [AllowAny]
    def post(self, request):
        logout(request)

        return Response(status=status.HTTP_200_OK)
    
class SingupView(generics.CreateAPIView):
    serializer_class = ClienteSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated] #Solo usuarios logueados pueden ver.
    serializer_class = ClienteSerializer
    http_method_names = ['get', 'patch']
    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user
        
class ListarUsuarios(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    http_method_names = ['get']
    permission_classes = [IsAdminUser]
    def list(self, request):
        queryset = self.get_queryset()
        serializer = ClienteSerializer(queryset, many=True)
        if self.request.user.is_authenticated:
            return Response(serializer.data)