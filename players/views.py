from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from loginregistration.models import UserLoginReg
from players.models import PlayerList

# Create your views here.
def players(request):
  userLoggedIn = ""
  if "user" in request.session:
    userLoggedIn = UserLoginReg.objects.get(id=request.session['user'])
    if userLoggedIn:
      playersList = PlayerList.objects.filter(userid=None)
      context= {
        'playersList' : playersList,
        'user' : userLoggedIn,
        'request': request.session['user']
      }
    template = loader.get_template('players.html')
    if userLoggedIn:
      return HttpResponse(template.render(context, request))
  else:
    return redirect("loginregistration:login")

def team(request):
  userLoggedIn = ""
  if "user" in request.session:
    userLoggedIn = UserLoginReg.objects.get(id=request.session['user'])
    if userLoggedIn:
      
      context= {
        'user' : userLoggedIn,
        'request': request.session['user']
      }
    template = loader.get_template('team.html')
    if userLoggedIn:
      return HttpResponse(template.render(context, request))
  else:
    return redirect("loginregistration:login")


def addPlayer(request, id):
  if PlayerList.objects.filter(id=id).count() > 0:
    player = PlayerList.objects.get(id=id)
    player.userid = int(request.session["user"])
    player.save()
    return redirect("players:players")
  else:
    return redirect("homepage:homepage")