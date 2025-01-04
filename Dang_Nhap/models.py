from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    favorite_game = models.CharField(max_length=100, blank=True, null=True)
    high_score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
