from django.urls import path
from jewelry_store import views


urlpatterns = [
    path("", views.ProductsView.as_view()),
    path("<slug:slug>/", views.ProductDetailView.as_view(), name="product_detail")
]
