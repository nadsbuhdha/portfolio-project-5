from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag',{})
    if not bag:
        messages.error(request, "There's currently nothing in the bag.")
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LADABADMfjFKo77lLFhiREBU980UGGcU6sw43e75qFFFaXYwiaYlBkrjbVNG7mWAOy9awYPhnFqGRsmCZ12fG2W00t9o01UUr'
    }

    return render(request, template, context)