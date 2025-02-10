from django.http import HttpResponse
from django.template import loader
from .models import Game
from .models import User
from .models import Assets
from django.contrib import messages
from datetime import date
from django.shortcuts import render, redirect

def games(request):
  mygames = Game.objects.all().values()
  template = loader.get_template('all_games.html')
  context = {
    'mygames' : mygames,
  }
  return HttpResponse(template.render(context, request))

def assets(request):
  myassets = Assets.objects.all().values()
  template = loader.get_template('assets.html')
  context = {
    'myassets' : myassets,
  }
  return HttpResponse(template.render(context, request))

def minigames(request):
  template = loader.get_template('minigames.html')
  return HttpResponse(template.render())

def freegames(request):
  mygames = Game.objects.filter(price=0).values()
  template = loader.get_template('free.html')
  context = {
    'mygames' : mygames,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mygame = Game.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mygame': mygame,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def player(request):
  template = loader.get_template('player.html')
  return HttpResponse(template.render())

def developer(request):
  template = loader.get_template('developer.html')
  return HttpResponse(template.render())

def designer(request):
  template = loader.get_template('designer.html')
  return HttpResponse(template.render())

def register(request):
  if request.method == 'POST':
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone')
      password = request.POST.get('password')
      role = request.POST.get('role')
      isPlayer = role == 'player'
      isDeveloper = role == 'developer'
      isDesigner = role == 'designer'
      if not name:
        messages.error(request, "Tên không được để trống.")
        return render(request, 'register.html')
      if not password:
        messages.error(request, "MK không được để trống.")
        return render(request, 'register.html')
      if User.objects.filter(email=email).exists():
        messages.error(request, "Email đã được sử dụng.")
        return render(request, 'register.html')
      if sum([isPlayer, isDeveloper, isDesigner]) == 0 :
        messages.error(request, "chọn 1 vai trò.")
        return render(request, 'register.html')
      else:
        user = User(name=name, email=email, phone=phone, password=password, isPlayer=isPlayer, isDeveloper=isDeveloper, isDesigner=isDesigner)
        user.save()
        return redirect('login')
      
  return render(request, 'register.html')

def login(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
      user = User.objects.get(email=email)
      if user.password == password:
        request.session['user_email'] = user.email
        if user.isPlayer == 1:
          return redirect('player')
        if user.isDesigner == 1:
          return redirect('designer')
        if user.isDeveloper == 1:
          return redirect('developer')
      else:
        messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng!")
    except User.DoesNotExist:
      messages.error(request, "Email không tồn tại!")
  return render(request, 'login.html')

def profiles(request):
  myprofiles = User.objects.all().values()
  template = loader.get_template('profiles.html')
  context = {
    'myprofiles' : myprofiles,
  }
  return HttpResponse(template.render(context, request))

def uploadgame(request):
  if request.method == 'POST':
      name = request.POST.get('name')
      price = request.POST.get('price')
      capacity = request.POST.get('capacity')
      release_date = date.today().strftime('%Y-%m-%d')
      if not name:
        messages.error(request, "Tên không được để trống.")
        return render(request, 'uploadgame.html')
      if not price:
        messages.error(request, "price không được để trống.")
        return render(request, 'uploadgame.html')
      if not capacity:
        messages.error(request, "capacity không được để trống.")
        return render(request, 'uploadgame.html')
      else:
        max_id = Game.objects.all().order_by('-id').first()
        new_id = max_id.id + 1 if max_id else 1
        game = Game(id= new_id, name=name, price=price, capacity=capacity, release_date=release_date)
        game.save()
        return redirect('developer')
      
  return render(request, 'uploadgame.html')

def uploadasset(request):
  if request.method == 'POST':
      name = request.POST.get('name')
      size = request.POST.get('size')
      type = request.POST.get('type')
      if not name:
        messages.error(request, "Tên không được để trống.")
        return render(request, 'uploadasset.html')
      if not size:
        messages.error(request, "size không được để trống.")
        return render(request, 'uploadasset.html')
      if not type:
        messages.error(request, "type không được để trống.")
        return render(request, 'uploadasset.html')
      else:
        max_id = Assets.objects.all().order_by('-id').first()
        new_id = max_id.id + 1 if max_id else 1
        asset = Assets(id= new_id, name=name, size=size, type=type)
        asset.save()
        return redirect('designer')
      
  return render(request, 'uploadasset.html')

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))