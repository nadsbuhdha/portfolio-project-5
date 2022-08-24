""" products admin """

from django.contrib import admin
from .models import Product, Category, Brand, Review
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """ products admin """
    list_display = (
        'sku',
        'name',
        'price',
        'rating',
        'image',
        'brand',
        'gender',
    )


class CategoryAdmin(admin.ModelAdmin):
    """ category admin """
    list_display = (
        'friendly_name',
        'name'
    )


class BrandAdmin(admin.ModelAdmin):
    """ brand admin """
    list_display = (
        'friendly_name',
        'name'
    )


class ReviewAdmin(admin.ModelAdmin):
    """ review admin """
    list_display = (
        'user',
        'product',
        'review_body',
        'created_on',
    )


admin.site.register(Review, ReviewAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
