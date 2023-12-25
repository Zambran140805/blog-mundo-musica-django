from django.contrib import admin
from . models import Usuario

# Register your models here.
@admin.register(Usuario)

class UsuarioAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'is_staff', 'role')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'role')
    search_fields = ('username', 'email','role')
    ordering = ('username', 'role')
    list_editable = ('role',)
