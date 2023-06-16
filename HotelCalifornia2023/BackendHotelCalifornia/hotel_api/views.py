from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ReservaSerializer

class ReservaView(generics.CreateAPIView):
    serializer_class = ReservaSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            fechaIngreso = serializer.validated_data['fechaIngreso']
            fechaEgreso = serializer.validated_data['fechaEgreso']
            
            if fechaEgreso <= fechaIngreso:
                return Response({'error': 'Fecha de egreso debe ser posterior a la fecha de ingreso.'}, status=status.HTTP_400_BAD_REQUEST)

            if fechaIngreso < serializer.instance.reservaId.fechaReserva:
                return Response({'error': 'No se puede reservar una habitación para una fecha anterior a la fecha de reserva.'}, status=status.HTTP_400_BAD_REQUEST)
            
            self.perform_create(serializer)            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)