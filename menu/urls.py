from django.urls import path
from .views import CategoriesListApiView, ProductsListApiView


urlpatterns = [
    path("categories/", CategoriesListApiView.as_view()),
    path("products/", ProductsListApiView.as_view()),
]