from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView
from django.contrib import messages
from django.db.models import Q
from .models import Product, Brand, Category

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    brands = None
    categories = None
    gender = None
    gender_type = []

    if request.GET:
        
        if 'brand' in request.GET:
            brands = request.GET['brand'].split(',')
            products = products.filter(brand__name__in=brands)
            brands = Brand.objects.filter(name__in=brands)

        
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)


        if 'gender' in request.GET:
            gender = request.GET['gender'].split(',')
            products = products.filter(gender__in=gender)

            if 'm' in gender:
                gender_type.append("Men's")
            if 'w' in gender:
                gender_type.append("Women's")


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a word to search")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) |Q(brand__name__icontains=query)
            products = products.filter(queries)
            

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'brands': brands,
        'gender': gender,
        'gender_type': gender_type,
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