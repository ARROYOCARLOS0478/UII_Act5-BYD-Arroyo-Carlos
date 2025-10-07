from django.db import models

# Create your models here.

class Producto(models.Model):
    # 1. CharField para el nombre del producto
    nombre = models.CharField(max_length=200)

    # 2. TextField para una descripción más larga
    descripcion = models.TextField(blank=True, null=True)

    # 3. DecimalField para el precio (con precisión)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    
    def __str__(self):
        return self.nombre


