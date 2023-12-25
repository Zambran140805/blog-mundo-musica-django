from django.urls import path, include
from .views import panel_colaboradores, post_template, eliminar_post, editar_post, eliminar_comentario,editar_comentario

urlpatterns = [
    path('panel-colaboradores/', panel_colaboradores, name='panel-colaboradores'),
    path('posts/<int:post_id>/', post_template, name='post-detail'),
    path('posts/<int:post_id>/delete/', eliminar_post, name='eliminar-post'),
    path('posts/<int:post_id>/edit/', editar_post, name='editar-post'),
    path('posts/<int:post_id>/comentarios/<int:comentario_id>/delete/', eliminar_comentario, name='eliminar-comentario'),
     path('posts/<int:post_id>/comentarios/<int:comentario_id>/editar/', editar_comentario, name='editar-comentario'),
]