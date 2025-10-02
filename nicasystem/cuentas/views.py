# cuentas/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomAuthenticationForm, RegistroForm

def panel(request):
    ctx = {
        'login_form': CustomAuthenticationForm(request),
        'registro_form': RegistroForm(),
        'active_tab': request.GET.get('tab', 'login'),
    }
    return render(request, 'cuentas/panel.html', ctx)

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())

            # "Recordarme" (opcional): si está marcado, sesión de 30 días; si no, expira al cerrar navegador.
            if request.POST.get('remember'):
                request.session.set_expiry(60 * 60 * 24 * 30)
            else:
                request.session.set_expiry(0)

            return redirect('home')
        # errores → quedarnos en el panel (pestaña login)
        ctx = {'login_form': form, 'registro_form': RegistroForm(), 'active_tab': 'login'}
        return render(request, 'cuentas/panel.html', ctx)
    return redirect('panel_cuentas')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        # errores → quedarnos en el panel (pestaña registro)
        ctx = {'login_form': CustomAuthenticationForm(request),
                'registro_form': form, 'active_tab': 'reg'}
        return render(request, 'cuentas/panel.html', ctx)
    return redirect('panel_cuentas')
