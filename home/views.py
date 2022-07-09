from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    """
    Class based view to return index page
    """

    template_name = 'home/index.html'
