from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROL_CHOICES = [
        ('cliente', 'Cliente'),
        ('ejecutivo', 'Ejecutivo'),
        ('logistica', 'Logistica'),
        ('finanzas', 'Finanzas'),
    ]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    productos = models.ManyToManyField(Producto)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField()
