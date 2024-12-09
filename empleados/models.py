from django.db import models


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return self.nombre

