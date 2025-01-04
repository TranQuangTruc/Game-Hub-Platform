from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'), 
    path('<str:role>/<int:user_id>/', views.userprofile, name='userprofile'),
]
