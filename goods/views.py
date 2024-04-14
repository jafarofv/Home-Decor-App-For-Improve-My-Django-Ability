from django.shortcuts import render

def catalog(request):
    context = {
        'title': 'Catalog',
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    context = {
        'title': 'Product',
    }
    return render(request, 'goods/product.html', context)