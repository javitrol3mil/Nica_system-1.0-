from django.shortcuts import redirect, render, get_object_or_404
from catalogo.models import Product


CART_KEY = 'cart_items' # dict: {product_id: qty}

def _get_cart(session):
    return session.setdefault(CART_KEY, {})

def agregar(request, product_id):
    cart = _get_cart(request.session)
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session.modified = True
    return redirect('carrito_ver')

def quitar(request, product_id):
    cart = _get_cart(request.session)
    cart.pop(str(product_id), None)
    request.session.modified = True
    return redirect('carrito_ver')

def vaciar(request):
    request.session[CART_KEY] = {}
    request.session.modified = True
    return redirect('carrito_ver')

def ver_carrito(request):
    cart = _get_cart(request.session)
    ids = [int(k) for k in cart.keys()]
    productos = Product.objects.filter(id__in=ids)
    items = []
    total = 0
    for p in productos:
        qty = cart.get(str(p.id), 0)
        subtotal = p.price * qty
        total += subtotal
        items.append({'p': p, 'qty': qty, 'subtotal': subtotal})
    return render(request, 'carrito/ver.html', {'items': items, 'total': total})
