from django.http import HttpResponse
from django.template import loader
from .models import Game

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

def testing(request):
  mygames = Game.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mygames': mygames,
  }
  return HttpResponse(template.render(context, request))