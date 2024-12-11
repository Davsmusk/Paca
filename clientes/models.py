from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)  # Añadir el campo telefono
    direccion = models.CharField(max_length=255)  # Añadir el campo direccion

    def __str__(self):
        return self.nombre
