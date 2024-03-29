"""
home/urls.py: all urls for the home app.
"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('newsletter', views.newsletter_signup, name='newsletter'),
    path('newsletter/unsubscribe', views.newsletter_unsub,
         name='newsletter_unsub'),
]
