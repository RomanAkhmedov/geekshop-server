# import json
# import os
# from geekshop.settings import JSON_DIR
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import TemplateView

from common.views import CommonContextMixin
from products.models import ProductCategory, Product


# Json-file unpacking.
# with open(os.path.join(JSON_DIR, 'products.json')) as file:
#    products_information = json.load(file)


class IndexView(CommonContextMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'GeekShop'


# def index(request):
#     context = {
#         'title': 'GeekShop'
#     }
#     return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    context = {'title': 'GeekShop - Каталог', 'categories': ProductCategory.objects.all()}
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    context.update({'products': products})

    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator
    return render(request, 'products/products.html', context)
