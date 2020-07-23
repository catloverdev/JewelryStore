from django.urls import path
from jewelry_store import views


urlpatterns = [
    path("", views.CategoriesProductView.as_view(), name='home'),
    path("category/<int:pk>/", views.product_list, name='product_list'),
    path("products/<int:pk>/", views.product_detail, name="product_detail"),
    path("create/", views.client_order_create, name="order_create"),
]
