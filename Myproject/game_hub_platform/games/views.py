from django.http import HttpResponse
from django.template import loader
from .models import Game
from .models import User
from django.contrib import messages
from django.shortcuts import render, redirect

def games(request):
  mygames = Game.objects.all().values()
  template = loader.get_template('all_games.html')
  context = {
    'mygames' : mygames,
  }
  return HttpResponse(template.render(context, request))

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

def register(request):
  if request.method == 'POST':
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone')
      if not name:
        messages.error(request, "Tên không được để trống.")
        return render(request, 'register.html')
      if User.objects.filter(email=email).exists():
        messages.error(request, "Email đã được sử dụng.")
      else:
        user = User(name=name, email=email, phone=phone)
        user.save()
        messages.success(request, "Đăng ký thành công!")
        return redirect('main')
  return render(request, 'register.html')

def login(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
      user = User.objects.get(email=email)
      if user.password == password:
        request.session['user_email'] = user.email
        messages.success(request, "Đăng nhập thành công!")
        return redirect('home')
      else:
        messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng!")
    except User.DoesNotExist:
      messages.error(request, "Email không tồn tại!")
  return render(request, 'login.html')

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))