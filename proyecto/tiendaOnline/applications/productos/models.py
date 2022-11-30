from email.policy import default
from django.db import models
from applications.users.models import User

# Create your models here.
class Categoria(models.Model):
    name = models.CharField('Nombre', max_length=50)
    anulate = models.BooleanField('Anulado', default=False)

    def __str__(self):
        return self.name

class Producto(models.Model):
    name = models.CharField('Nombre', max_length=60)
    price = models.FloatField("Precio")
    image = models.CharField('Imagen', max_length=200)
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    amount = models.IntegerField('Cantidad')

    def __str__(self):
        return self.name 
    
class Carrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.IntegerField('Cantidad',default=0)

    def __str__(self):
        return self.producto.name