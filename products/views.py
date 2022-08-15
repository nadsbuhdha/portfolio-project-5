from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView
from profiles.models import Favourites
from django.contrib import messages
from django.http import Http404
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from .models import Product, Brand, Category, Review
from .forms import ProductForm, ReviewForm
from django.core.exceptions import PermissionDenied
# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    brands = None
    categories = None
    gender = None
    gender_type = []
    sort = None
    direction = None


    try:
        favourites = get_object_or_404(Favourites, user=request.user.id)
    except Http404:
        favourites = {}
        favourites = None
    else:
        favourites = favourites.product.all()

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
        
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
            

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'brands': brands,
        'gender': gender,
        'gender_type': gender_type,
        'current_sorting': current_sorting,
        'favourites': favourites,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    product detail view
    """

    try:
        favourites = get_object_or_404(Favourites, user=request.user.id)
    except Http404:
        favourites = {}
        favourites = None
    else:
        favourites = favourites.product.all()

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)
    review_form = ReviewForm(data=request.POST or None)
    # user_comments = product.reviews.filter(user=request.user)
    # if request.method == 'POST':

        # review_form = ReviewForm(data=request.POST or None)
        # if user_comments:
        #         # Users cant review once
        #         messages.error(request, "You have already reviewed this product")
        #         return redirect(reverse('product_detail', args=[product.id]))
                


    #     if request.user.is_authenticated and review_form.is_valid():

    #         review_form.instance.user = request.user
    #         review = review_form.save(commit=False)
    #         review.product = product
    #         review.save()
    #         messages.success(
    #             request, (
    #                 f'Thank you for reviewing "{product.name[:25]}.."! '
    #                 'You can now view and remove it below.'
    #             )
    #         )
    #     return redirect(reverse('product_detail', args=[product.id]))
    # else:
    # review_form = ReviewForm()

    context = {
        'product': product,
        'favourites': favourites,
        'reviews': reviews,
        'review_form': review_form,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))


    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)
    user_comments = product.reviews.filter(user=request.user)
    if request.method == 'POST':

        review_form = ReviewForm(data=request.POST or None)
        if user_comments:
                # Users cant review once
                messages.error(request, "You have already reviewed this product")
                return redirect(reverse('product_detail', args=[product.id]))
                


        if request.user.is_authenticated and review_form.is_valid():

            review_form.instance.user = request.user
            review = review_form.save(commit=False)
            review.product = product
            review.save()
            messages.success(
                request, (
                    f'Thank you for reviewing "{product.name[:25]}.."! '
                    'You can now view and remove it below.'
                )
            )
        return redirect(reverse('product_detail', args=[product.id]))
    else:
        review_form = ReviewForm()    



@login_required
def delete_review(request, product_id, review_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = get_object_or_404(Review, product=product, user__username=review_id)
    review_form = ReviewForm(data=request.POST or None)

    if request.user == reviews.user:
        if request.method == 'POST':
            review_form.instance.user = request.user
            reviews.product = product
            reviews.delete()
            messages.success(
                request, (
                    'your review has been deleted'))     
        else:
            messages.error(request, 'Invalid request')
        return redirect(reverse('product_detail', args=[product.id]))
    else:
        messages.error(request, "Sorry, you don't have permission to do that.")
        return redirect(reverse('product_detail', args=[product.id]))