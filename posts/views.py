from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from . models import Post, Categoria
from comentarios.models import Comentario
from comentarios.forms import ComentarioForm
from . forms import PostForm
from django.contrib import messages


# Create your views here.
def es_colaborador(user):
    return user.role == 'colaborador'

@user_passes_test(es_colaborador)
def panel_colaboradores(request):
    context = {}
    
    categorias = Categoria.objects.all()
    categoria_seleccionada = request.GET.get('categoria')

    orden = request.GET.get('orden', 'asc_titulo')

    
    if categoria_seleccionada:
        posts = Post.objects.filter(categoria__nombre=categoria_seleccionada)
    else:
        posts = Post.objects.all()


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

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Post creado exitosamente!')
            return redirect('panel-colaboradores')  # Redirige a la vista del panel
        else:
            messages.error(request, '¡Algo salió mal!')
    else:
        form = PostForm()

    context['form'] = form

    return render(request, 'panel/panel-colaboradores.html', context)



def post_template(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comentarios = Comentario.objects.filter(post=post).order_by('fecha_comentario')


    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.autor = request.user
            comentario.save()
            return redirect('post-detail', post_id=post_id)
    else:
        form = ComentarioForm()

    contexto = {'post': post, 'comentarios': comentarios, 'form': form}

    return render(request, 'posts/post-template.html', contexto)


@user_passes_test(es_colaborador)
def eliminar_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('panel-colaboradores')

def eliminar_comentario(request, comentario_id, post_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id)
    comentario.delete()
    return redirect('post-detail', post_id=post_id)

@user_passes_test(es_colaborador)
def editar_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('panel-colaboradores')
    
    else:
        form = PostForm(instance=post)

    return render(request, 'panel/editar-post.html', {'form': form, 'post': post})


def editar_comentario(request, comentario_id, post_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id)
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.autor = request.user
            comentario.save()
            return redirect('post-detail', post_id=post_id)
    else:
        form = ComentarioForm()
    return render(request, 'panel/editar-comentario.html', {'comentario': comentario, 'form': form})