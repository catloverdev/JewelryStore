from django.shortcuts import render
from jewelry_store.models import Purchase, AllPurchases, Status
from cart.cart import Cart
from jewelry_store.forms import ClientCreateForm
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
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'jewelry_store/product_detail.html', context)


def main_page(request):
    return render(request, "jewelry_store/main_page.html")


def client_order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = ClientCreateForm(request.POST)
        if form.is_valid():
            client = form.save()
            purchase = Purchase.objects.create(id_purchase=Purchase.objects.count() + 1,
                                               client=client)
            Status.objects.create(purchase=purchase)
            for item in cart:
                AllPurchases.objects.create(purchase=purchase,
                                            product=item['product'],
                                            price=item['price'],
                                            amount=item['quantity'])
            cart.clear()
            return render(request, 'jewelry_store/created.html', {'client': client,
                                                                  'order': purchase})
    else:
        form = ClientCreateForm
    return render(request, 'jewelry_store/create.html', {'cart': cart,
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


class PriceListView(APIView):
    def get(self, request):
        prices = ProductPrice.objects.all()
        serializer = PriceListSerializer(prices, many=True)
        return Response(serializer.data)


class PriceDetailView(APIView):
    def get(self, request, pk):
        price = ProductPrice.objects.filter(product__id_product=pk)
        serializer = PriceDetailSerializer(price, many=True)
        return Response(serializer.data)


class ClientListView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientListSerializer(clients, many=True)
        return Response(serializer.data)


class ClientDetailView(APIView):
    def get(self, request, pk):
        client = Client.objects.get(purchase__id_purchase=pk)
        serializer = ClientDetailSerializer(client)
        return Response(serializer.data)


class StatusListView(APIView):
    def get(self, request):
        status = Status.objects.all()
        serializer = StatusListSerializer(status, many=True)
        return Response(serializer.data)


class StatusDetailView(APIView):
    def get(self, request, pk):
        status = Status.objects.filter(purchase__id_purchase=pk)
        serializer = StatusDetailSerializer(status, many=True)
        return Response(serializer.data)


class CreateStatusView(APIView):
    """Создание статуса"""
    def post(self, request):
        serializer = StatusCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
