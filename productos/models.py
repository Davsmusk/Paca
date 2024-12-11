from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    existencia = models.IntegerField(default=0)  # Valor por defecto para existencia
    descripcion = models.TextField(default='')  # Valor por defecto para descripcion
    imagen = models.ImageField(upload_to='images/', default='images/default.png')  # Valor por defecto para imagen

    def __str__(self):
        return self.nombre
