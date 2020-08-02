from django.urls import path, include
from jewelry_store import views


urlpatterns = [
    path("", views.main_page, name='home'),
    path("category/<int:pk>/", views.product_list, name='product_list'),
    path("products/<int:pk>/", views.product_detail, name="product_detail"),
    path("create/", views.client_order_create, name="order_create"),
    path("get_products/", views.ProductListView.as_view()),
    path("get_products/<int:pk>", views.ProductDetailView.as_view()),
    path('create_price/', views.PriceCreateView.as_view()),
    path('get_statuses/', views.StatusListView.as_view()),
    path('create_status/', views.StatusCreateView.as_view()),
    path('get_purchases/', views.PurchaseListView.as_view()),
    path('get_purchases/<int:pk>', views.PurchaseDetailView.as_view()),
]
