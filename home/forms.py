""" home forms """

from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    """ newsletter form """
    class Meta:
        """ meta data """
        model = Newsletter
        fields = ['email', ]
