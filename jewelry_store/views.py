from django.shortcuts import render
from jewelry_store.models import Purchase, AllPurchases, Status
from django.views.generic import ListView
from cart.cart import Cart
from jewelry_store.forms import ClientCreateForm
# Create your views here.

from jewelry_store.models import Product, CategoriesProduct
from cart.forms import CartAddProductForm


def product_list(request, pk):
    categories = CategoriesProduct.objects.all()
    products = Product.objects.filter(category=pk)
    context = {
        'products': products,
        'categoriesproduct_list': categories
    }
    return render(request, 'jewelry_store/product_list.html', context)


def product_detail(request, pk):
    categories = CategoriesProduct.objects.all()
    product = Product.objects.get(id_product=pk)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'categoriesproduct_list': categories,
        'cart_product_form': cart_product_form
    }
    return render(request, 'jewelry_store/product_detail.html', context)


class CategoriesProductView(ListView):
    """Категории"""
    model = CategoriesProduct
    queryset = CategoriesProduct.objects.all()
    template_name = "jewelry_store/main_page.html"


def client_order_create(request):
    categories = CategoriesProduct.objects.all()
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
                                                                  'order': purchase,
                                                                  'categoriesproduct_list': categories})
    else:
        form = ClientCreateForm
    return render(request, 'jewelry_store/create.html', {'cart': cart,
                                                         'form': form,
                                                         'categoriesproduct_list': categories})
