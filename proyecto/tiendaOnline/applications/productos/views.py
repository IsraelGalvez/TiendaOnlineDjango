from django.views.generic import (
    ListView
)

from .models import Producto ,Carrito
from applications.users.models import User
from django.views.generic import View
# Create your views here.

class listAllProducts(ListView):
    template_name = 'products/main.html'
    model = Producto

class listProductsCategory(ListView):
    """ Lista los productos por categoria"""
    template_name = 'products/playeras.html'
    queryset = Producto.objects.filter(
        categorias__name ="Playeras"
    )

class listProductsCategoryJeans(ListView):
    """ Lista los productos por categoria"""
    template_name = 'products/pantalones.html'
    queryset = Producto.objects.filter(
        categorias__name ="Pantalones"
    )

class listProductsCategorySueter(ListView):
    """ Lista los productos por categoria"""
    template_name = 'products/sudaderas.html'
    queryset = Producto.objects.filter(
        categorias__name ="Sudaderas"
    )

class ProductView(ListView):
    """ Trae la informacion de un producto con el id """
    template_name = 'products/producto.html'

    def get_queryset(self):
        pk = self.kwargs['pk']
        lista = Producto.objects.filter(
            id = pk
        )   
        return lista


class CarritoProducts(ListView):
    template_name = 'products/carrito.html'
    model = Producto

class AddProductToCar(View):
    model = Carrito

