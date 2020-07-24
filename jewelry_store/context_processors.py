from jewelry_store.models import CategoriesProduct


def categories(request):
    my_categories = CategoriesProduct.objects.all()
    return {'my_categories': my_categories}
