from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorting = request.GET.get('sort')
    if sorting == 'name':
        phones = Phone.objects.order_by('name')
    elif sorting == 'max_price':
        phones = Phone.objects.order_by('-price')
    elif sorting == 'min_price':
        phones = Phone.objects.order_by('price')
    else:
        phones = Phone.objects.all()
    context = {
        'phones': [{
            'name': p.name,
            'price': p.price,
            'image': p.image,
            'slug': p.slug,
        } for p in phones]
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': {
            'name': phone.name,
            'price': phone.price,
            'image': phone.image,
            'release_date': phone.release_date,
        }
    }
    return render(request, template, context)
