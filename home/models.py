from django.db import models

class Newsletter(models.Model):
    """ A model for users to subscribe to a newsletter """

    email = models.EmailField(max_length=254, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email