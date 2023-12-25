from django import forms
from .models import Post, Categoria
from usuarios.models import Usuario


class PostForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), to_field_name='nombre')
    autor = forms.ModelChoiceField(queryset=Usuario.objects.filter(role='colaborador'), to_field_name='username')

    class Meta:
        model = Post
        fields = ('portada', 'titulo', 'texto', 'categoria', 'autor')

        
