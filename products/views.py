from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Programme

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and searching """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            category = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories':categories,
    }

    return render(request, 'products/products.html', context)

def all_programmes(request):
    """ A view to return the programmes """

    programmes = Programme.objects.all()

    context = {
        'programmes': programmes
    }

    return render(request, 'products/programmes.html', context)



def product_detail(request, product_id):
    """ A view to show product detail """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def programme_detail(request, programme_id):
    """ A view to show programme detail """

    programme = get_object_or_404(Programme, pk=programme_id)

    context = {
        'programme': programme,
    }

    return render(request, 'products/programme_detail.html', context)


def search_results(request):
    """ A view to return search results """

    products = Product.objects.all()
    programmes = Programme.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            programmes = programmes.filter(category__name__in=categories)
            category = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products')) # Note: Might need to update this to search_results instead of products
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            programmes = programmes.filter(queries)

        context = {
            'products': products,
            'programmes': programmes,
            'search_term': query,
            'current_categories':categories,
        }

    return render(request, 'products/search_results.html', context)