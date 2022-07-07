# Credits: This code is sourced & adapted from the
# Code Institute Boutique Ado Project
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals
