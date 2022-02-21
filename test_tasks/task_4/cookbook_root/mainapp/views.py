from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from mainapp.models import Recipe, Category, Ingredient
import random


def get_today_list():
    """Возварщает срисок случайных объектов из последних обновленных"""
    today_list = Recipe.objects.filter(is_active=True).order_by('-time_update')[:5]
    return random.sample(list(today_list), 2)


def main(request):
    title = 'главная'
    recipes = Recipe.objects.filter(is_active=True)[:8]
    ingredients = Ingredient.objects.all()
    today_list = get_today_list()
    links_menu = Category.objects.all()

    try:
        item_id = int(request.GET.get('ingredient', None))
    except (ValueError, TypeError):
        item_id = None
    if item_id:
        ingredient = Ingredient.objects.get(id=item_id)
        recipes = ingredient.recipes.all()

    context = {
        'title': title,
        'recipes': recipes,
        'today_list': today_list,
        'links_menu': links_menu,
        'ingredients': ingredients,
        'item_id': item_id,
    }
    return render(request, 'mainapp/index.html', context)


def categories(request, pk=None, page=1):
    title = 'Рецепты'
    links_menu = Category.objects.all()
    context = {
        'title': title,
        'links_menu': links_menu,
    }
    if pk is not None:
        category = get_object_or_404(Category, pk=pk)
        recipes = Recipe.objects.filter(category_id=pk, is_active=True)

        paginator = Paginator(recipes, 4)
        try:
            recipes_paginator = paginator.page(page)
        except PageNotAnInteger:
            recipes_paginator = paginator.page(1)
        except EmptyPage:
            recipes_paginator = paginator.page(paginator.num_pages)

        context['category'] = category
        context['recipes'] = recipes_paginator

    return render(request, 'mainapp/categories.html', context)


def recipe(request, pk=None):
    links_menu = Category.objects.all()
    recipe = get_object_or_404(Recipe, pk=pk)
    title = recipe.name
    ingredients = recipe.ingredients.all()
    context = {
        'title': title,
        'recipe': recipe,
        'links_menu': links_menu,
        'ingredients': ingredients,
    }
    return render(request, 'mainapp/recipe.html', context)
