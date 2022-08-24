""" products form """

from django import forms
from .models import Product, Category, Brand, Review
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """product form """
    class Meta:
        """ meta data """
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        brands = Brand.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'


class ReviewForm(forms.ModelForm):
    """
    A form to review products
    """
    class Meta:
        """
        the meta class for the review form
        """
        model = Review
        fields = (
            'review_body',
        )
