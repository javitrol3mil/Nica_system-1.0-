# cuentas/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Usuario',
            'autocomplete': 'username',
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Contraseña',
            'autocomplete': 'current-password',
        })

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre', max_length=30, required=False)
    last_name  = forms.CharField(label='Apellido', max_length=30, required=False)
    email      = forms.EmailField(label='Email', required=False)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Usuario (sin espacios)',
            'autocomplete': 'username',
        })
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Nombre'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Apellido'})
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email',
            'autocomplete': 'email'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Contraseña',
            'autocomplete': 'new-password',
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Repetir contraseña',
            'autocomplete': 'new-password',
        })
