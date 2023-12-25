from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from pyexpat import model

class FormularioDeCreacionDeUsuarios(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']
    
    # password1 = forms.CharField(widget=forms.PasswordInput())