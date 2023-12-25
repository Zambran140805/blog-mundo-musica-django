from django.contrib import admin
from . models import Comentario

# Register your models here.
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):

    list_display = ('autor', 'post', 'texto', 'fecha_comentario')
    list_filter = ('autor', 'post', 'texto', 'fecha_comentario')
    search_fields = ('autor', 'post', 'texto', 'fecha_comentario')

