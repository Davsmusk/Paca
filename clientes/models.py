from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField(default="No especificada")  # Definir un valor predeterminado

    def __str__(self):
        return self.nombre
