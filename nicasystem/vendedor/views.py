from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from catalogo.models import Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = '/cuentas/panel/' #importante
    model = Product
    fields = ['name', 'price', 'description', 'image_url', 'featured', 'category', 'tags']
    success_url = reverse_lazy('catalogo_lista')
    template_name = 'vendedor/producto_form.html'