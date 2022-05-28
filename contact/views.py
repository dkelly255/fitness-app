from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact

# Create your views here.

# def contact_view(request):
#     """ A view to return the contact form page """

#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('success'))

#     form = ContactForm()

#     context = {'form': form}
    
#     return render(request, 'contact/contact.html', context)

def contact_view(request):
    """ A view to return the contact form page to site visitors """

    if not request.user.is_anonymous:
        user = get_object_or_404(User, username=request.user) 
        print("here")
        form = ContactForm(initial={'first_name': request.user.first_name, 'last_name':request.user.last_name, 'email':request.user.email })    
        print("and here")
    else:
        form = ContactForm(request.POST or None)  

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print("Got to here")
            return redirect(reverse('success'))
            print("And to here")
    
    context = {'form': form}

    return render(request, 'contact/contact.html', context)

def enquiry_log(request):

    enquiries = Contact.objects.all()

    context = {
                'enquiries': enquiries
                }

    return render(request, 'contact/enquiry_log.html', context)


def success(request):
    """ A view that renders the success page """

    return render(request, 'contact/success.html')