from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import UserProfileForm
from django.http import Http404
from django.contrib import messages
from products.models import Product
from checkout.models import Order
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


from .models import UserProfile, Favourites

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)


    try:
        favourites = Favourites.objects.filter(user=request.user.id)[0]
    except IndexError:
        favourites_items = None
    else:
        favourites_items = favourites.product.all()

    if not favourites_items :
        messages.info(request, 'Your favourites is empty!')

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'favourites_items':favourites_items
    }

    return render(request, template, context)



def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request, (
            f'This is a past confirmation for order number {order_number}.'
                'A confirmation email was sent on the order date.'))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


# @login_required
# def add_to_favourites(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     favourites = get_object_or_404(Favourites, user=request.user)
#     if product.favourites.filter(id=request.user.id).exists():
#         product.favourites.remove(request.user)
#         messages.success(request, product.name + " has been removed from your WishList")
#     else:
#         product.favourites.add(request.user)
#         messages.success(request, "Added " + product.name + " to your WishList")
#     return redirect(reverse('product', args=[product_id]))
    

@login_required
def add_to_favourites(request, product_id):
    """
    Adds the product to the users Wishlist.
    Args:
        request (the request object)
        product_id (the product in question)
    Returns:
        the MyStepUp profile page
    """
    product = get_object_or_404(Product, pk=product_id)
    try:
        favourites = get_object_or_404(Favourites, user=request.user.id)

    except Http404:
        favourites = Favourites.objects.create(user=request.user)
    if product in favourites.product.all():
        messages.info(request, 'Your Wishlist contains this product already,')
    else:
        favourites.product.add(product)
        messages.info(
            request, f'Added {product.name[:30]}.. favourites.'
        )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_favourites(request, product_id):
    """
    Removes a product from the users Wishlist.
    Args:
        request (the request object)
        product_id (the product in question)
    Returns:
        A redirect to the previously viewed page
    """
    product = get_object_or_404(Product, pk=product_id)
    favourites = get_object_or_404(Favourites, user=request.user.id)
    if product in favourites.product.all():
        favourites.product.remove(product)
        messages.info(
            request, f'Removed {product.name[:30]} from your favourites'
        )
    else:
        messages.error(
            request, (
                f'{product.name[:30]}.. is not in your favourites'
            )
        )

    # Return the previously viewed page
    return redirect(request.META.get('HTTP_REFERER'))