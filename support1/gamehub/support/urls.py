from django.urls import path
from .views import submit_support_request

urlpatterns = [
    path('', submit_support_request, name='submit_support'),
]

