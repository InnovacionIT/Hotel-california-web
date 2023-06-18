from django.db import models
from ..GestionReservas.models import Habitacion
from ..GestionReservas.models import Servicio


class ServicioPorHabitacion(models.Model):
    servicioPorHabitacionId = models.AutoField(primary_key=True)
    servicioId = models.ForeignKey(Servicio, to_field='servicioId', on_delete=models.CASCADE)
    habitacionId = models.ForeignKey(Habitacion, to_field='habitacionId', on_delete=models.CASCADE)

    class Meta:
        db_table = "ServicioPorHabitacion"
        verbose_name = "Servicio de cada habitación"
        verbose_name_plural = "ServiciosPorHabitacion"

    def __str__(self):
        return f"Servicio {self.servicioId} de la habitación {self.habitacionId}"

