from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def contact_view(request):
    """ A view to return the contact form page to site visitors """

    if not request.user.is_anonymous:
        user = get_object_or_404(User, username=request.user)
        form = ContactForm(initial={'first_name': request.user.first_name, 'last_name': request.user.last_name, 'email': request.user.email})
    else:
        form = ContactForm(request.POST or None)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Enquiry was submitted! Please allow one working day for processing and reply')
            
            send_mail(
                'Subject here',
                'Here is the message.',
                settings.DEFAULT_FROM_EMAIL,
                request.POST.get("id_email")
            )   

            return redirect(reverse('home'))

    context = {'form': form}

    return render(request, 'contact/contact.html', context)


def enquiry_log(request):

    enquiries = Contact.objects.all()
    enquiries = enquiries.order_by('-date_submitted')

    paginator = Paginator(enquiries, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
                'enquiries': enquiries,
                'page_obj': page_obj,
                }

    return render(request, 'contact/enquiry_log.html', context)


def action_enquiry(request, enquiry_id):
    """ A view to open/close enquiries """

    enquiry = get_object_or_404(Contact, id=enquiry_id)
    enquiry.status = not enquiry.status
    enquiry.save()

    return redirect(reverse('enquiry_log'))
