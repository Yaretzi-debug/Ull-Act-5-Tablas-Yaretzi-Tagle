from django.db import models

# Create your models here.
#clase habitaciones
class Habitaciones(models.Model):
    numero=models.CharField(max_length=100)
    capacidad=models.IntegerField()
    numero=models.EmailField(unique=True)

def __str__(self):
    return f"(self.numero) {self.capacidad}"
