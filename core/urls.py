from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Inicio.as_view(), name='home'),
    path('acerca-de/', AcercaDe.as_view(), name='about'),
    path('contacto/', Contacto.as_view(), name='contacto'),
    path('categorias/', CategoriasPosts.as_view(), name='categorias'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.logout_then_login, name='logout'),


    #includes
    path('registro/', include('usuarios.urls')),
    path('posts/', include('posts.urls')),
]
