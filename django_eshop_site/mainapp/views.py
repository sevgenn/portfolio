from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
import json
import os
import random
from eshop.settings import BASE_DIR

from mainapp.models import Product, ProductCategory
from basketapp.models import Basket


def get_hot_product():
    products_list = Product.objects.filter(category__is_active=True)
    return random.sample(list(products_list), 1)[0]


def get_same_products(hot_product):
     same_products = Product.objects.filter(category=hot_product.category, is_active=True).\
         exclude(pk=hot_product.pk)[:3]
     return same_products


def main(request):
    title = 'главная'
    products = Product.objects.filter(category__is_active=True)[:3]
    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None, page=1):
    title = 'продукты'
    links_menu = ProductCategory.objects.filter(is_active=True)
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    context = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
    }

    if pk is not None:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = Product.objects.filter(category_id=pk, is_active=True,
                    category__is_active=True).order_by('price')

        paginator = Paginator(products, 3)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context['category'] = category
        context['products'] = products_paginator
        return render(request, 'mainapp/products_list.html', context)

    # same_products = []
    # products_path = os.path.join(BASE_DIR, 'mainapp/json_files/same_products.json')
    # if os.path.exists(products_path):
    #     with open(products_path, encoding='utf-8') as f:
    #         same_products = json.load(f)
    # same_products = Product.objects.all()[:3]

    # context['same_products'] = same_products
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    title = 'контакты'
    location = []
    location_path = os.path.join(BASE_DIR, 'mainapp/json_files/location.json')
    if os.path.exists(location_path):
        with open(location_path, encoding='utf-8') as f:
            location = json.load(f)
    context = {
        'title': title,
        'location': location,
    }
    return render(request, 'mainapp/contacts.html', context)


def product(request, pk):
    title = 'продукты'
    links_menu = ProductCategory.objects.filter(is_active=True)
    product = get_object_or_404(Product, pk=pk)
    context = {
        'title': title,
        'product': product,
        'links_menu': links_menu
    }
    return render(request, 'mainapp/product.html', context)
