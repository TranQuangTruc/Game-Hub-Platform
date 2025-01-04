from django.contrib import admin
from .models import UserProfile  # Import model UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'favorite_game', 'high_score')
    
    search_fields = ('user__username', 'favorite_game') 
    
    list_filter = ('favorite_game', 'high_score')

admin.site.register(UserProfile, UserProfileAdmin)
