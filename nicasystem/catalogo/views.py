from django.shortcuts import render, get_object_or_404
from .models import Product, Category




def lista_productos(request):
    q = request.GET.get('q', '')
    productos = Product.objects.select_related('category').prefetch_related('tags')
    if q:
        productos = productos.filter(name__icontains=q)
    return render(request, 'catalogo/lista.html', {'productos': productos, 'q': q})




def detalle_producto(request, slug):
    producto = get_object_or_404(Product.objects.select_related('category').prefetch_related('tags'), slug=slug)
    relacionados = Product.objects.filter(category=producto.category).exclude(id=producto.id)[:4]
    return render(request, 'catalogo/detalle.html', {'p': producto, 'relacionados': relacionados})