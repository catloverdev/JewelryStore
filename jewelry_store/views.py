from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
# Create your views here.

from jewelry_store.models import Product, CategoriesProduct


def product_list(request, pk, slug):
    categories = CategoriesProduct.objects.all()
    products = Product.objects.filter(category=pk)
    context = {
        'product_list': products,
        'categories_list': categories
    }
    return render(request, 'jewelry_store/product_list.html', context)


def product_detail(request, pk):
    categories = CategoriesProduct.objects.all()
    product = Product.objects.get(id_product=pk)
    context = {
        'product': product,
        'categories_list': categories
    }
    return render(request, 'jewelry_store/product_detail.html', context)


class CategoriesProductView(ListView):
    """Категории"""
    model = CategoriesProduct
    queryset = CategoriesProduct.objects.all()
    template_name = "jewelry_store/main_page.html"
