from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from jewelry_store.models import Product, CategoriesProduct
from cart.cart import Cart
from cart.forms import CartAddProductForm
# Create your views here.


@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, id_product=pk)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'])
        cart.save()
    return redirect('cart:cart_detail')


def cart_remove(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, id_product=pk)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
