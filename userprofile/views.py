from django.shortcuts import render, get_object_or_404
from .models import Player, Admin, Designer, Developer
from django.contrib.auth.decorators import login_required

@login_required
def player_profile(request):
    player = get_object_or_404(Player, email=request.user.email)
    return render(request, 'player_profile.html', {'player': player})

@login_required
def admin_profile(request):
    admin = get_object_or_404(Admin, name=request.user.username)
    return render(request, 'admin_profile.html', {'admin': admin})

@login_required
def designer_profile(request):
    designer = get_object_or_404(Designer, email=request.user.email)
    return render(request, 'designer_profile.html', {'designer': designer})

@login_required
def developer_profile(request):
    developer = get_object_or_404(Developer, email=request.user.email)
    return render(request, 'developer_profile.html', {'developer': developer})
