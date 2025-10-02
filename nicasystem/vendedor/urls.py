from django.urls import path
from . import views


urlpatterns = [
    path('crear/', views.ProductCreateView.as_view(), name='vendedor_crear'),
]