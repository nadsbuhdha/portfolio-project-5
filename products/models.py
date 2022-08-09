from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """
    The Category model class & friendly name
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):
    """
    Brand Class
    """
    name = models.CharField(max_length=200)
    
    friendly_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


GENDER = (
    ('u', 'Unisex'),
    ('w', "Women's"),
    ('m', "Men's"),
)


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.SET_NULL)
    gender = models.CharField(choices=GENDER, max_length=10,default='u')
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    

    def __str__(self):
        return self.name



class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    review_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['created_on']
    
    def __str__(self):
        return f"Review {self.review_body} by {self.user}  "