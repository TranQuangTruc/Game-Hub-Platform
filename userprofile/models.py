from django.db import models
from games.models import Game, User          

class Player(models.Model):
    playerID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Admin(models.Model):
    adminID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Designer(models.Model):
    designerID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Developer(models.Model):
    developerID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)

    groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions_set", blank=True)

    def __str__(self):
        return self.username
