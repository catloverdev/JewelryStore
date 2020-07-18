from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.

from jewelry_store.models import Product


class ProductsView(View):
    """Категории"""
    def get(self, request):
        products = Product.objects.all()
        return render(request, "products/products_list.html", {"product_list": products})
