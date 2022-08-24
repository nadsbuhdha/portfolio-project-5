""" checkout app"""


from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ checkout configuration """
    name = 'checkout'

    def ready(self):
        import checkout.signals
