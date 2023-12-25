from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    role = models.CharField(max_length=50, null=False, default='miembro')
