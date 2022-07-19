"""
home/urls.py: all urls for the home app.
"""
# - - - - - Django Imports - - - - - - - - - - - - -
from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
]