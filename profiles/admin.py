from django.contrib import admin
from .models import Favourites

class FavouritesAdmin(admin.ModelAdmin):
    """
    Admin class for the Favourites model.
    """
    list_display = (
        'user',
    )
    search_fields = (
        'user',
    )
    list_filter = (
        'user',
    )
    list_per_page = 20


admin.site.register(Favourites, FavouritesAdmin)