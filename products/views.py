import json
import os
from django.shortcuts import render
from geekshop.settings import JSON_DIR

# Json-file unpacking.
with open(os.path.join(JSON_DIR, 'products.json')) as file:
    products_information = json.load(file)


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = products_information
    return render(request, 'products/products.html', context)
