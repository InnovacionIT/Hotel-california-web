from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import ReservaSerializer, ServicioSerializer
from GestionReservas.models import Reserva, Servicio
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

def validateDate(serializer):
    fechaReserva = serializer.validated_data['fechaReserva']
    fechaIngreso = serializer.validated_data['fechaIngreso']
    fechaEgreso = serializer.validated_data['fechaEgreso']

    if fechaEgreso <= fechaIngreso:
        return Response({'error': 'Fecha de egreso debe ser posterior a la fecha de ingreso.'}, status=status.HTTP_400_BAD_REQUEST)

    if fechaIngreso < fechaReserva:
        return Response({'error': 'No se puede reservar una habitación para una fecha anterior a la fecha de reserva.'}, status=status.HTTP_400_BAD_REQUEST)

class ReservaView(APIView):
    def get(self, request, reservaId=None):
        if reservaId is not None:  # Check if reservaId is provided
            return self.get_by_id(request, reservaId)
        reservas = Reserva.objects.all()
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_by_id(self, request, reservaId):
        reserva = get_object_or_404(Reserva, pk=reservaId)
        serializer = ReservaSerializer(reserva)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ReservaSerializer(data=request.data)
        if serializer.is_valid():
            response = validateDate(serializer)
            if response:
                return response
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, reservaId):
        reserva = get_object_or_404(Reserva, pk=reservaId)
        serializer = ReservaSerializer(reserva, data=request.data)
        if serializer.is_valid():
            response = validateDate(serializer)
            if response:
                return response
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, reservaId):
        reserva = get_object_or_404(Reserva, pk=reservaId)
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReservaCreateView(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            response = validateDate(serializer)
            if response:
                return response
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservaUpdateView(generics.UpdateAPIView):
    serializer_class = ReservaSerializer
    queryset = Reserva.objects.all()

    def perform_update(self, serializer):
        response = validateDate(serializer)
        if response:
            return response
        serializer.save()

class ReservaDetailView(generics.RetrieveAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    lookup_field = 'pk'

class ReservaDeleteView(generics.DestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    lookup_field = 'pk'


def obtener_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)
    serializer = ServicioSerializer(servicio)
    return Response(serializer.data)


def obtener_servicios(request):
    servicios = Servicio.objects.all()
    serializer = ServicioSerializer(servicios, many=True)
    return Response(serializer.data)
