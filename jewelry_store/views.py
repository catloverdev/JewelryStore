from django.shortcuts import render, get_object_or_404
from jewelry_store.models import Purchase, AllPurchases, Status
from cart.cart import Cart
from jewelry_store.forms import ClientCreateForm
import cart.forms
# Create your views here.

from cart.forms import CartAddProductForm

from rest_framework.response import Response
from rest_framework.views import APIView
from jewelry_store.serializer import *


def product_list(request, pk):
    products = Product.objects.filter(category=pk)
    context = {
        'products': products,
    }
    return render(request, 'jewelry_store/product_list.html', context)


def product_detail(request, pk):
    product = Product.objects.get(id_product=pk)
    cart_product_form = CartAddProductForm()
    cart_product_form.set_amount(product.amount_storage)
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'jewelry_store/product_detail.html', context)


def main_page(request):
    return render(request, "jewelry_store/main_page.html")


def client_order_create(request):
    my_cart = Cart(request)
    if request.method == 'POST':
        form = ClientCreateForm(request.POST)
        if form.is_valid():
            client = form.save()
            purchase = Purchase.objects.create(id_purchase=Purchase.objects.count() + 1,
                                               client=client)
            Status.objects.create(purchase=purchase)
            for item in my_cart:
                AllPurchases.objects.create(purchase=purchase,
                                            product=item['product'],
                                            price=item['price'],
                                            amount=item['quantity'])
            my_cart.clear()
            return render(request, 'jewelry_store/created.html', {'client': client,
                                                                  'order': purchase})
    else:
        form = ClientCreateForm
    return render(request, 'jewelry_store/create.html', {'cart': my_cart,
                                                         'form': form})


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    def get(self, request, pk):
        products = Product.objects.get(id_product=pk)
        serializer = ProductDetailSerializer(products)
        return Response(serializer.data)


class PriceCreateView(APIView):
    def post(self, request):
        serializer = PriceCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)


class StatusListView(APIView):
    def get(self, request):
        statuses = Status.objects.all()
        serializer = StatusListSerializer(statuses, many=True)
        return Response(serializer.data)


class StatusCreateView(APIView):
    def post(self, request):
        serializer = StatusCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)


class PurchaseListView(APIView):
    def get(self, request):
        purchases = Purchase.objects.all()
        serializer = PurchaseListSerializer(purchases, many=True)
        return Response(serializer.data)


class PurchaseDetailView(APIView):
    def get(self, request, pk):
        purchase = Purchase.objects.get(id_purchase=pk)
        serializer = PurchaseDetailSerializer(purchase)
        return Response(serializer.data)
