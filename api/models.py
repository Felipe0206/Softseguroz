from django.db import models

# Create your models here.
from django.db import models

class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    numero_documento = models.CharField(max_length=20)
    rol = models.CharField(max_length=20, choices=(('cliente', 'Cliente'), ('administrador', 'Administrador')))
