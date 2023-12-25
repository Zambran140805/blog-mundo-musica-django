from django.views.generic.edit import CreateView
from .models import Usuario
from .forms import FormularioDeCreacionDeUsuarios
from django.template import RequestContext
from django.urls import reverse

# Create your views here.

class CrearUsuario(CreateView):
    model = Usuario
    form_class = FormularioDeCreacionDeUsuarios
    template_name = 'registro/registro-usuarios.html'

    def get_success_url(self, **kwargs):
        return reverse('home')