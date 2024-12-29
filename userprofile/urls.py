from django.urls import path
from . import views

urlpatterns = [
    path('player/profile/', views.player_profile, name='player_profile'),
    path('admin/profile/', views.admin_profile, name='admin_profile'),
    path('designer/profile/', views.designer_profile, name='designer_profile'),
    path('developer/profile/', views.developer_profile, name='developer_profile'),
]
