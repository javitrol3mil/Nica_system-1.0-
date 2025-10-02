from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_productos, name='catalogo_lista'),
    path('<slug:slug>/', views.detalle_producto, name='catalogo_detalle'),
]