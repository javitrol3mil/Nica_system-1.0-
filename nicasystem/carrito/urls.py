from django.urls import path
from . import views


urlpatterns = [
    path('', views.ver_carrito, name='carrito_ver'),
    path('agregar/<int:product_id>/', views.agregar, name='carrito_agregar'),
    path('quitar/<int:product_id>/', views.quitar, name='carrito_quitar'),
    path('vaciar/', views.vaciar, name='carrito_vaciar'),
]