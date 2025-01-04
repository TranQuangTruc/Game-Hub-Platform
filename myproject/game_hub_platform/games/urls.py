from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('games/', views.games, name='games'),
    path('f2p/', views.freegames, name='f2p'),
    path('games/details/<int:id>', views.details, name='details'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'), 
    path('testing/', views.testing, name='testing'),
  

]



