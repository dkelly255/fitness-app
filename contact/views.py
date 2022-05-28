from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact

# Create your views here.

def contact_view(request):
    """ A view to return the contact form page to site visitors """

    if not request.user.is_anonymous:
        user = get_object_or_404(User, username=request.user) 
        form = ContactForm(initial={'first_name': request.user.first_name, 'last_name':request.user.last_name, 'email':request.user.email })    
    else:
        form = ContactForm(request.POST or None)  

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()            
            return redirect(reverse('success'))            
    
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


def action_enquiry(request, enquiry_id):
    """ A view to open/close enquiries """
    
    enquiry = get_object_or_404(Contact, id=enquiry_id)
    print(f'enquiry = {enquiry}')
    print(enquiry.status)
    print(enquiry.id)
    print("HELLO")
    print(request)
    print(request.user)
    # enquiry = get_object_or_404(Contact, id=item_id)
    # enquiry.status = not enquiry.status
    # enquiry.save()

    enquiry.status = not enquiry.status
    enquiry.save()

    return redirect(reverse('enquiry_log'))