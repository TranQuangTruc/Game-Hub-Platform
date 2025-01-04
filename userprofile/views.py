# views.py
from django.shortcuts import render, get_object_or_404
from .models import Admin, Player, Designer, Developer
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

#def userprofile(request):
    #print(request.user)  # In thông tin người dùng ra console
    #return render(request, 'userprofile.html')

def main(request):
  template = loader.get_template('userprofile.html')
  return HttpResponse(template.render())
def userprofile(request, role, user_id):
    user = None
    if role == "admin":
        user = get_object_or_404(Admin, adminID=user_id)
    elif role == "player":
        user = get_object_or_404(Player, playerID=user_id)
    elif role == "designer":
        user = get_object_or_404(Designer, designerID=user_id)
    elif role == "developer":
        user = get_object_or_404(Developer, developerID=user_id)
    else:
        return render(request, '404.html', {'error': 'Invalid role'})

    return render(request, 'userprofile.html', {'user': user, 'role': role})
