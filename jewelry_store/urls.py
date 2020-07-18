from django.urls import path
from jewelry_store import views


urlpatterns = [
    path("", views.ProductsView.as_view())
]

