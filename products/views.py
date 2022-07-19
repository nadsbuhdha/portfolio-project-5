from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """
    product detail view
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)