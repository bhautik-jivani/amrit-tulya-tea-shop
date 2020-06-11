from django.urls import path
from .views import *


urlpatterns = [
    path('', dahsboard),
    path('add-product/', add_product),
    path('product/<int:prod_id>/view/', view_product),
    path('product/<int:prod_id>/remove/', remove_product),
] 