from django.db import models

# Create your models here.
class Pedido(models.Model): 
    nPedido = models.CharField(max_length=100)
    fechaCreacion = models.CharField(max_length=100)
    precioSnImp = models.CharField(max_length=100)
    porcentajeImp = models.CharField(max_length=100)
    precioCnImuesto = models.CharField(max_length=100)
    moneda = models.CharField(max_length=100)

class Articulo(models.Model): 
    identificador = models.CharField(max_length=100)
    nombreArticulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    unidades = models.CharField(max_length=100)
    precioSnImuesto = models.CharField(max_length=100)

    
