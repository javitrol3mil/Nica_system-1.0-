from django.shortcuts import render
from catalogo.models import Product, Category


def home(request):
    featured = Product.objects.filter(featured=True).select_related('category').first()
    categories = Category.objects.all()
    return render(request, 'core/home.html', {
        'featured': featured,
        'categories': categories,
})
