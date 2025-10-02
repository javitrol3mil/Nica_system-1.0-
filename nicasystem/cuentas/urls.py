# cuentas/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('panel/', views.panel, name='panel_cuentas'),

    path('login/', views.login_view, name='login'),     # ← personalizado
    path('registro/', views.registro, name='registro'), # ← personalizado
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # POST
]
