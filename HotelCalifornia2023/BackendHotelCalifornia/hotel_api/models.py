from django.db import models
from GestionReservas.models import Servicio
from GestionReservas.models import Habitacion
from GestionReservas.models import ServicioPorHabitacion

class Meta:
        db_table = "ServicioPorHabitacion"
        verbose_name = "Servicio de cada habitación"
        verbose_name_plural = "ServiciosPorHabitacion"

def __str__(self):
    return f"Servicio {self.servicioId} de la habitación {self.habitacionId}"

