from django.db import models

class Game(models.Model):
  id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=255)
  price = models.IntegerField(null=True)
  capacity = models.CharField(max_length=10)
  release_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.name}"

class FreeGame(models.Model):
  id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=255)
  price = models.IntegerField(null=True)
  capacity = models.CharField(max_length=10)
  release_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.name}"