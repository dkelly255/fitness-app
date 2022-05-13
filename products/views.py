from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Programme
from .forms import ProductForm

# Create your views here.

def all_products(request):
    """ A view to show all products, and filter by category note:searching by term has been extracted out into search_results view """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        
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

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def all_programmes(request):
    """ A view to return the programmes and filter by category note:searching by term has been extracted out into search_results view"""

    programmes = Programme.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

   
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = programmes.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            programmes = programmes.order_by(sortkey)

        
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            programmes = programmes.filter(category__name__in=categories)
            category = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('programmes'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            programmes = programmes.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'programmes': programmes,
        'search_term': query,
        'current_categories':categories,
        'current_sorting': current_sorting,
    }

    print(categories)

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


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)