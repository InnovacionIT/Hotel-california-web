from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import ReservaSerializer
from GestionReservas.models import Reserva

class ReservaCreateView(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            fechaReserva = serializer.validated_data['fechaReserva']
            fechaIngreso = serializer.validated_data['fechaIngreso']
            fechaEgreso = serializer.validated_data['fechaEgreso']

            if fechaEgreso <= fechaIngreso:
                return Response({'error': 'Fecha de egreso debe ser posterior a la fecha de ingreso.'}, status=status.HTTP_400_BAD_REQUEST)

            if fechaIngreso < fechaReserva:
                return Response({'error': 'No se puede reservar una habitación para una fecha anterior a la fecha de reserva.'}, status=status.HTTP_400_BAD_REQUEST)
            
            self.perform_create(serializer)            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservaUpdateView(generics.UpdateAPIView):
    serializer_class = ReservaSerializer
    queryset = Reserva.objects.all()

    def perform_update(self, serializer):
        if serializer.is_valid():
            fechaReserva = serializer.validated_data['fechaReserva']
            fechaIngreso = serializer.validated_data['fechaIngreso']
            fechaEgreso = serializer.validated_data['fechaEgreso']

            if fechaEgreso <= fechaIngreso:
                return Response({'error': 'Fecha de egreso debe ser posterior a la fecha de ingreso.'}, status=status.HTTP_400_BAD_REQUEST)

            if fechaIngreso < fechaReserva:
                return Response({'error': 'No se puede reservar una habitación para una fecha anterior a la fecha de reserva.'}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ReservaDetailView(generics.RetrieveAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    lookup_field = 'pk'

class ReservaDeleteView(generics.DestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    lookup_field = 'pk'