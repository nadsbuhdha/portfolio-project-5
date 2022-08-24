""" home admin """

from django.contrib import admin
from .models import Newsletter


class NewsletterAdmin(admin.ModelAdmin):
    """Newsletter Admin """
    list_display = (
        'email', 'date_added',)

    search_fields = ('email', 'date_added',)


admin.site.register(Newsletter, NewsletterAdmin)
