from django.forms import ModelForm
from django.db import models
from django import forms
from .models import Contact


class ContactForm(ModelForm):  
    # first_name = models.CharField(max_length=100, null=True, blank=True)
    # last_name = models.CharField(max_length=100, null=True, blank=True)
    # email = models.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    # subject = models.CharField(max_length=255)
    # message = models.TextField()
    
    
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'email',
            'subject',
            'message',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['message'].widget.attrs.update({'class': 'form-control'})