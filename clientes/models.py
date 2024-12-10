from django.db import models

from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # Otros campos relevantes

    def __str__(self):
        return self.nombre

