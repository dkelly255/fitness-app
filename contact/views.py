from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.

def contact_view(request):
    """ A view to return the contact form page """

    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
