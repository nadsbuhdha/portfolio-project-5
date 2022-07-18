from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product

# Create your views here.

def all_products(request):
    """
    all products view
    """

    products = Product.objects.all()


    context = {'products' : products
    
    }
    return render(request, 'products/products.html', context)