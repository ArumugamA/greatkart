from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import Category
# Create your views here.
def store(request, category_slug=None):
    category = None
    products = None

    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
    else:
        products = Product.objects.filter(is_available=True)
    context = {'products': products}
    return render(request, 'store/store.html', context)
