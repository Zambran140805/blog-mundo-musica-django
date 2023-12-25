from django.contrib import admin
from . models import Post, Categoria

# Register your models here.@admin.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'categoria')
    list_filter = ('autor', 'fecha_publicacion', 'categoria')
    search_fields = ('titulo', 'autor__username', 'categoria__nombre')
    list_editable = ('autor', 'categoria')
    list_display_links = ('titulo',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
  
   
  
