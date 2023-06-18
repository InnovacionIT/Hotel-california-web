from django.urls import path
from .views import ReservaUpdateView, ReservaCreateView, ReservaDetailView, ReservaDeleteView, ReservaView, FacturaView, FacturaCreateView, DetallePagoView, DetalleView

# urlpatterns = [
#     path('reserva/', ReservaCreateView.as_view(), name='reserva'),
#     path('reserva/<int:pk>/', ReservaUpdateView.as_view(), name='reserva-actualizar'),
#     path('reserva/detalle/<int:pk>/', ReservaDetailView.as_view(), name='reserva-detalle'),
#     path('reserva/delete/<int:pk>/', ReservaDeleteView.as_view(), name='reserva-delete'),
# ]

urlpatterns = [
    path('reserva/', ReservaCreateView.as_view(), name='reserva_lista'),
    path('reserva/<int:reservaId>/', ReservaView.as_view(), name='reserva'),
    path('factura/', FacturaView.as_view(), name='factura_lista'),
    path('factura/<int:facturaId>/', FacturaView.as_view(), name='factura'),
    path('detalle/', DetalleView.as_view(), name='detalle_lista'),
    path('detalle/<int:detalleId>/', DetalleView.as_view(), name='detalle'),
    path('detallePago/', DetallePagoView.as_view(), name='detalle_pago_lista'),
    path('detallePago/<int:detallePagoId>/', DetallePagoView.as_view(), name='detalle_pago'),
]