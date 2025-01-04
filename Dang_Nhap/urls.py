from django.urls import path
from .views import login_view

urlpatterns = [
    # Các URL khác
    path('login/', login_view, name='login'),
]
