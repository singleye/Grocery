from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser
#from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class MyUser(AbstractBaseUser):
    username = models.CharField(unique=True,
            max_length=255,
            blank=False,
            null=False,
            error_messages={
            'unique':'User already existed!'
            })
    mobile = models.CharField(max_length=16,
            blank=True,
            null=True)
    email = models.EmailField(max_length=65,
            blank=True,
            null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['']

#class UserProfile(models.Model):
#    user = models.OneToOneField(User,
#            unique=True,
#            db_column='user')
#    mobile = models.CharField(max_length=255,
#            blank=False,
#            null=False)
#    role = models.IntegerField(blank=False)
