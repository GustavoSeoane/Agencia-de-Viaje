from django.db import models
from django.utils.timezone import now

class Viaje (models.Model):
    precio = models.FloatField()
    destino = models.CharField(max_length=50)
    fecha_salida = models.DateField(default=now)
    fecha_regreso = models.DateField(null=True, blank=True)


class Destino (models.Model):
    name = models.CharField(max_length=50)