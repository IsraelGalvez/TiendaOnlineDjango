from codecs import mbcs_decode
from email.policy import default
from django.db import models

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
        return self.name + '-' + self.categorias.name + "-" + str(self.amount)