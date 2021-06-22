# import json
# import os
# from geekshop.settings import JSON_DIR
from django.shortcuts import render
from products.models import ProductCategory, Product


# Json-file unpacking.
# with open(os.path.join(JSON_DIR, 'products.json')) as file:
#    products_information = json.load(file)


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    context = {'title': 'GeekShop - Каталог', 'categories': ProductCategory.objects.all()}
    context.update({
        'products': Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    })
    return render(request, 'products/products.html', context)
