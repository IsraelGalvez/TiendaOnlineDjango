import imp
from django.urls import path
from . import views

app_name = 'product_app'

urlpatterns = [
    path('',views.listAllProducts.as_view(),name="home"),
    path('playeras/',views.listProductsCategory.as_view(),name="playeras"),
    path('pantalones/',views.listProductsCategoryJeans.as_view(),name="pantalones"),
    path('sudaderas/',views.listProductsCategorySueter.as_view(),name="sudaderas"),
]