from django.urls import path

# Internal:
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag')]