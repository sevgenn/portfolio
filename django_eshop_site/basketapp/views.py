from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.urls import reverse
from basketapp.models import Basket
from mainapp.models import Product


@login_required
def basket(request):
    title = 'корзина'
    basket_items = Basket.objects.filter(user=request.user)
    context = {
        'title': title,
        'basket_items': basket_items,
    }
    return render(request, 'basketapp/basket.html', context)


@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[pk]))
    product = get_object_or_404(Product, pk=pk)

    basket_item = Basket.objects.filter(user=request.user, product=product).first()
    if not basket_item:
        basket_item = Basket(user=request.user, product=product)

    basket_item.quantity += 1
    basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        basket_item = Basket.objects.get(pk=int(pk))

        if quantity > 0:
            basket_item.quantity = quantity
            if basket_item.quantity > basket_item.product.quantity:
                basket_item.quantity = basket_item.product.quantity
            basket_item.save()
        else:
            basket_item.delete()

        basket_items = Basket.objects.filter(user=request.user)
        context = {
            'basket_items': basket_items
        }

        result = render_to_string('basketapp/includes/inc_basket_list.html', context)

        return JsonResponse({'result': result})


@login_required
def basket_remove(request, pk):
    basket_item = get_object_or_404(Basket, pk=pk)
    basket_item.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
