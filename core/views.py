from django.views.generic import TemplateView
from django.contrib.auth import login, logout
from posts.models import Post, Categoria

class Inicio(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categorias = Categoria.objects.all()
        categoria_seleccionada = self.request.GET.get('categoria')

        orden = self.request.GET.get('orden', 'asc_titulo')


        if categoria_seleccionada:
            posts = Post.objects.filter(categoria__nombre=categoria_seleccionada).order_by('fecha_publicacion')
        else:
            posts = Post.objects.all().order_by('fecha_publicacion')

        
        if 'asc_titulo' in orden:
            posts = posts.order_by('titulo')
        elif 'desc_titulo' in orden:
            posts = posts.order_by('-titulo')
        elif 'asc_fecha' in orden:
            posts = posts.order_by('fecha_publicacion')
        elif 'desc_fecha' in orden:
            posts = posts.order_by('-fecha_publicacion')



        context['posts'] = posts
        context['categorias'] = categorias
        context['categoria_seleccionada'] = categoria_seleccionada
        context['orden'] = orden

        return context

class AcercaDe(TemplateView):
    template_name = 'acerca-de.html'

class Contacto(TemplateView):
    template_name = 'contacto.html'


class CategoriasPosts(TemplateView):
    template_name = 'categorias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categorias = Categoria.objects.all()
        posts_por_categoria = {}

        for categoria in categorias:
            posts = Post.objects.filter(categoria=categoria).order_by('fecha_publicacion')
            posts_por_categoria[categoria] = posts


        context['posts_por_categoria'] = posts_por_categoria
      

        return context