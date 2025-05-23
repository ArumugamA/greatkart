from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import Category
from cart.models import CartItem
from cart.views import _cart_id
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.
def store(request, category_slug=None):
    category = None
    products = None

    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True).order_by('id')
        paginator = Paginator(products, 1)
        # page = request.GET.get('page')
        # paged_products = paginator.get_page(page)
    else:
        products = Product.objects.filter(is_available=True).order_by('id')
        paginator = Paginator(products, 3)
    
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()
    context = {
        'products': paged_products,
        'product_count': product_count,
        }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=product).exists()
    except Exception as e:
        raise e

    context = {
        'product': product,
        'in_cart': in_cart,
    }
    return render(request, 'store/product_detail.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.filter(Q(name__icontains=keyword) | Q(description__icontains=keyword)).order_by('-created_at')
        else:
            products = Product.objects.all().order_by('-created_at')
    product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
        }
    return render(request, 'store/store.html', context)