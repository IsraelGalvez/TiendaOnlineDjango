from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]
    objects = UserManager()

    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos
