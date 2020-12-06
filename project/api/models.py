from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager



# Create your models here.



class UserProfileManager(BaseUserManager):

    def create_user(self,email,name,username,password=None):
        user=self.model(email=email,name=name,username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,email,name,username,password):
        user=self.create_user(email,name,username,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user





class UserProfile(AbstractBaseUser,PermissionsMixin):
    name=models.CharField(max_length=75)
    username=models.CharField(unique=True,max_length=50)
    email=models.EmailField( unique=True,max_length=254)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    objects=UserProfileManager()

    USERNAME_FIELD='email'
    USERNAME_FIELD='username'

    REQUIRED_FIELDS=['name']

    def __str__(self):
        return self.name
