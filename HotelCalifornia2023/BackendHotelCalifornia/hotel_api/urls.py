from django.urls import path
from .views import ReservaUpdateView, ReservaCreateView, ReservaDetailView, ReservaDeleteView, ReservaView

# urlpatterns = [
#     path('reserva/', ReservaCreateView.as_view(), name='reserva'),
#     path('reserva/<int:pk>/', ReservaUpdateView.as_view(), name='reserva-actualizar'),
#     path('reserva/detalle/<int:pk>/', ReservaDetailView.as_view(), name='reserva-detalle'),
#     path('reserva/delete/<int:pk>/', ReservaDeleteView.as_view(), name='reserva-delete'),
# ]

urlpatterns = [
    path('reserva/', ReservaView.as_view(), name='reserva_list'),
    path('reserva/<int:reservaId>/', ReservaView.as_view(), name='reserva_detail'),
]