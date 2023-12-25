from django.db import models
from django.conf import settings

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    portada = models.TextField()
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='autor')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria')

    def __str__(self):
        return self.titulo



    

 
    