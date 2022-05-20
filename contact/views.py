from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def contact_view(request):
    """ A view to return the index page """

    return render(request, 'contact/contact.html')
