from django.shortcuts import render
from product.models import AC, AcCategory


# Create your views here.


def product_category_view(request):
    category = AcCategory.objects.all()
    context = {
        'page_title': 'AC Category\'s',
        'category': category
    }
    return render(request, 'product/product_category.html', context)


def product_ifo_form_category(request, category_name):
    lists = AC.objects.filter(ac_category__ac_category_name=category_name)
    context = {
        'list': lists,
        'page_title': f'Details/{category_name}'
    }

    return render(request, 'product/product_details_boc.html', context)


def product_details_bosc(request, product_name):
    ac_details = AC.objects.filter(ac_name__exact=product_name)
    return render(request, 'product/product_details.html', {'ac_details': ac_details})


def all_product_view(request):
    food_detail = AC.objects.all()
    return render(request, 'product/all_product.html', {'products': food_detail})
