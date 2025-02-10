from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('player/', views.player, name='player'),
    path('games/', views.games, name='games'),
    path('games/details/<int:id>', views.details, name='details'),

    path('developer/', views.developer, name='developer'),
    path('uploadgame/', views.uploadgame, name='uploadgame'),
    path('assets/', views.assets, name='assets'),

    path('designer/', views.designer, name='designer'),
    path('uploadasset/', views.uploadasset, name='uploadasset'),
    
    path('minigames/', views.minigames, name='minigames'),
    path('f2p/', views.freegames, name='f2p'),
    path('f2p/details/<int:id>', views.details, name='details'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'), 
    path('profiles/', views.profiles, name='profiles'),
    path('testing/', views.testing, name='testing'),
]