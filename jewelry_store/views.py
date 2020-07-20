from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
# Create your views here.

from jewelry_store.models import Product


class ProductsView(ListView):
    """Список товаров"""
    model = Product
    queryset = Product.objects.all()
    # template_name = "jewelry_store/index.html"


class ProductDetailView(DetailView):
    """"Полное описание изделия"""
    model = Product
    slug_field = "url"
