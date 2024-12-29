from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('games/', views.games, name='games'),
    path('f2p/', views.freegames, name='f2p'),
    path('games/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),    
]