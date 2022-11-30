from django.views.generic import (
    ListView, CreateView, FormView
)

from .models import Producto ,Carrito
from applications.users.models import User
from django.views.generic import View
from django.shortcuts import render
from .forms import CarritoForm
from django.urls import reverse_lazy
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

class ProductView(FormView):
    """ Trae la informacion de un producto con el id """
    template_name = 'products/producto.html'
    form_class = CarritoForm
    success_url = reverse_lazy('product_app:carrito')

    # def get_queryset(self):
    #     pk = self.kwargs['pk']
    #     lista = Producto.objects.filter(
    #         id = pk
    #     )
    #     return lista
    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context["object_list"] = Producto.objects.filter(
            id =pk
        )

        return context

    
    def form_valid(self, form):
        usuario = self.request.user
        print("-------------------------------------------")
        print(usuario)
        producto = form.cleaned_data['producto']
        cantidad = form.cleaned_data['cantidad']
        obj, created = Carrito.objects.get_or_create(
            producto = producto,
            defaults={
                'producto': Producto.objects.get(id=producto),
                'cantidad': cantidad,
                'usuario': usuario
            }
        )

        if not created:
            obj.cantidad = obj.cantidad + cantidad
            obj.save()
        return super(ProductView, self).form_valid(form)

    

class CarritoProducts(ListView):
    template_name = 'products/carrito.html'
    model: Carrito
    success_url = '.'
    def get_queryset(self):
        return Carrito.objects.filter(usuario=self.request.user)


