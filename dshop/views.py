from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Article
from cart.forms import CartAddProductForm


def index(request):
    template = 'dshop/index.html'
    articles = Article.objects.all().order_by('published_at')
    return render(request, template,
                  context={'articles': articles})


def product_list(request, slug='root'):
    template = 'dshop/product/list.html'
    products = Product.objects.filter(available=True)
    category = get_object_or_404(Category, slug=slug)
    products = products.filter(category__in=category.get_descendants(include_self=True))
    return render(request, template,
                  {'category': category,
                   'products': products})


def product_detail(request, slug):
    template = 'dshop/product/detail.html'
    product = get_object_or_404(Product,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, template,
                  {'product': product,
                   'cart_product_form': cart_product_form})


def articles_list(request):
    template = 'dshop/articles_list.html'
    articles = Article.objects.all()
    return render(request, template,
                  context={
                      'articles': articles})


def articles_detail(request, slug):
    template = 'dshop/article_detail.html'
    article = get_object_or_404(Article,
                                slug=slug)
    return render(request, template,
                  {'article': article})
