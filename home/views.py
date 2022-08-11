from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from .models import Newsletter
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import NewsletterForm
# Create your views here.

class HomeView(TemplateView):
    """
    Class based view to return index page
    """

    template_name = 'home/index.html'



def newsletter_signup(request):
    """ A view to handle the customer newsletter subscription """
    form = NewsletterForm()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if Newsletter.objects.filter(
                    email=instance.email).exists():
                messages.error(request, 'You are already Subscribed')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                instance.save()
                messages.success(request, 'Thank you for subscribing to our \
                    newsletter!')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': form,
    }

    return render(request, 'home/newsletter.html', context)