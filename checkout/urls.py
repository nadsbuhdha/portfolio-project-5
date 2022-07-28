"""
checkout/urls.py: all urls for the home app.
"""
# - - - - - Django Imports - - - - - - - - - - - - -
from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
]