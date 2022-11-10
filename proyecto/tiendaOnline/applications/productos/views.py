from django.views.generic import (
    ListView
)

from .models import Producto
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

