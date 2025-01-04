from django.contrib import admin
from .models import Game

class GameAdmin(admin.ModelAdmin):
  list_display = ("name", "price", "capacity", "release_date",)

admin.site.register(Game, GameAdmin)