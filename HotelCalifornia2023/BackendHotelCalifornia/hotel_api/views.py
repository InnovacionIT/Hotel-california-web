from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import ReservaSerializer, FacturaSerializer, DetalleSerializer, DetallePagoSerializer
from GestionReservas.models import Reserva
from Facturacion.models import Factura, Detalle, DetallePago
from rest_framework.views import APIView

def validarFecha(serializer):
        fechaReserva = serializer.validated_data['fechaReserva']
        fechaIngreso = serializer.validated_data['fechaIngreso']
        fechaEgreso = serializer.validated_data['fechaEgreso']

        if fechaEgreso <= fechaIngreso:
            return Response({'error': 'Fecha de egreso debe ser posterior a la fecha de ingreso.'}, status=status.HTTP_400_BAD_REQUEST)

        if fechaIngreso < fechaReserva:
            return Response({'error': 'No se puede reservar una habitación para una fecha anterior a la fecha de reserva.'}, status=status.HTTP_400_BAD_REQUEST)
        
def tryGetById(clase, claseId):
    try:
        return clase.objects.get(pk=claseId)
    except clase.DoesNotExist:
        return None

class ReservaView(APIView):
    def get(self, request, reservaId=None):
        if reservaId is not None:  # Check if reservaId is provided
            return self.get_by_id(request, reservaId)
        reservas = Reserva.objects.all()
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_by_id(self, request, reservaId):
        reserva = tryGetById(Reserva, reservaId)
        if reserva is None:
            return Response({'error': 'Reserva not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReservaSerializer(reserva)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ReservaSerializer(data=request.data)
        if serializer.is_valid():
            validarFecha(serializer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, reservaId):
        reserva = tryGetById(Reserva, reservaId)
        if reserva is None:
            return Response({'error': 'Reserva not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReservaSerializer(reserva, data=request.data)
        if serializer.is_valid():
            validarFecha(serializer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, reservaId):
        reserva = tryGetById(Reserva, reservaId)
        if reserva is None:
            return Response({'error': 'Reserva not found'}, status=status.HTTP_404_NOT_FOUND)        
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FacturaView(APIView):
    def get(self, request, facturaId=None):
        if facturaId is not None:  # Check if reservaId is provided
            return self.get_by_id(request, facturaId)
        facturas = Factura.objects.all()
        serializer = FacturaSerializer(facturas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_by_id(self, request, facturaId):
        factura = tryGetById(Factura, facturaId)
        if factura is None:
            return Response({'error': 'Factura no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FacturaSerializer(factura)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = FacturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleView(APIView):
    def get(self, request, detalleId=None):
        if detalleId is not None:  # Check if reservaId is provided
            return self.get_by_id(request, detalleId)
        detalles = Detalle.objects.all()
        serializer = DetalleSerializer(detalles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_by_id(self, request, detalleId):
        detalle = tryGetById(Detalle, detalleId)
        if detalle is None:
            return Response({'error': 'Detalle no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DetalleSerializer(detalle)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = DetalleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DetallePagoView(APIView):
    def get(self, request, detallePagoId=None):
        if detallePagoId is not None:  # Check if reservaId is provided
            return self.get_by_id(request, detallePagoId)
        detallesDePago = DetallePago.objects.all()
        serializer = DetallePagoSerializer(detallesDePago, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_by_id(self, request, detallePagoId):
        detallePago = tryGetById(DetallePago, detallePagoId)
        if detallePago is None:
            return Response({'error': 'Detalle de pago no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DetallePagoSerializer(detallePago)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = DetallePagoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    lookup_field = 'pk'