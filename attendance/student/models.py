from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import User

# Create your models here.

class Admin(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='admin_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='admin_permissions')
    username = models.CharField(max_length=20, null=True, unique=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)  # Use TimeField for time


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')
    username = models.CharField(max_length=20, null=True, unique=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)