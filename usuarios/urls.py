from django.urls import path, include
from .views import *

app_name='usuarios'

urlpatterns = [
    path('registro/', CrearUsuario.as_view(), name='registrar'),
]
