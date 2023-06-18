from django.urls import path
from .views import ReservaUpdateView, ReservaCreateView, ReservaDetailView, ReservaDeleteView, ReservaView
from .views import obtener_servicios
from .views import obtener_servicio

# urlpatterns = [
#     path('reserva/', ReservaCreateView.as_view(), name='reserva'),
#     path('reserva/<int:pk>/', ReservaUpdateView.as_view(), name='reserva-actualizar'),
#     path('reserva/detalle/<int:pk>/', ReservaDetailView.as_view(), name='reserva-detalle'),
#     path('reserva/delete/<int:pk>/', ReservaDeleteView.as_view(), name='reserva-delete'),
# ]

urlpatterns = [
    path('reserva/', ReservaView.as_view(), name='reserva_list'),
    path('reserva/<int:reservaId>/', ReservaView.as_view(), name='reserva_detail'),
    path('habitacion/<int:habitacion_id>/servicios/', obtener_servicios),
    path('servicio/<int:servicio_id>/', obtener_servicio),
]
