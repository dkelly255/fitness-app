from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact

# Create your views here.

def contact_view(request):
    """ A view to return the contact form page to site visitors """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/success.html')
    
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)

def enquiry_log(request):

    enquiries = Contact.objects.all()

    context = {
                'enquiries': enquiries
                }

    return render(request, 'contact/enquiry_log.html', context)
