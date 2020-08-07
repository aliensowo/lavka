from django.shortcuts import render
from .models import CategoriesProducts, ProductFB


def home_view(request):
    """Отображение стартовой страницы index.html"""
    return render(request, template_name='index.html')


def fb_view(request):
    """Конроллер для страницы фейсбук аккаунтов. рендрит страницу"""
    categories = CategoriesProducts.objects.all()
    products = ProductFB.objects.filter()

    return render(request, '1-1.html', {
        'categories': categories,
        'products': products,
    })
