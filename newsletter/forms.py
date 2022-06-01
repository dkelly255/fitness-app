from django.forms import ModelForm
from .models import Newsletter

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = (
            'email',
            'privacy',
        )