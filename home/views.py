""" homepage views """

from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Newsletter
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


def newsletter_unsub(request):
    """ A view to handle newsletter unsubscriptions """
    form = NewsletterForm()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if Newsletter.objects.filter(
                    email=instance.email).exists():
                Newsletter.objects.filter(
                    email=instance.email).delete()
                messages.success(request, 'You have successfully unsubscribed \
                    from our newsletter, we are sorry to see you go.')
                return redirect(reverse('home'))
            else:
                messages.error(request, 'Sorry but we did not find your email address. \
                    Please check it has been entered correctly.')

    context = {
        'form': form,
    }

    return render(request, 'home/newsletter_unsub.html', context)


def error_handle_404(request, exception):
    """ 404 handler """
    return render(request, '404.html')
