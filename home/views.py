from django.shortcuts import render, redirect, reverse
from newsletter.forms import NewsletterForm
from newsletter.models import Newsletter
from django.contrib import messages

# Create your views here.


def index(request):
    """ A view to return the index page """

    form = NewsletterForm(request.POST or None)

    if request.method == 'POST':
        print(form.errors)
        if form.is_valid:
            form.save()
            messages.success(request, 'Thank you for subscribing')
            return redirect(reverse('home'))
        messages.error(request, 'Sorry there was an error please try again')

    context = {
        'form': form,
    }

    return render(request, 'home/index.html', context)


def about(request):
    """ A view to return the index page """

    return render(request, 'home/about.html')
