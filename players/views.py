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
      if PlayerList.objects.filter(userid=request.session["user"]).count() > 0:
        playersList = PlayerList.objects.filter(userid=request.session["user"])
        context= {
          "playersList" : playersList,
          'user' : userLoggedIn,
          'request': request.session['user']
        }
      else:
        context= {
          'user' : userLoggedIn,
          'request': request.session['user']
        }
    template = loader.get_template('team.html')
    if userLoggedIn:
      return HttpResponse(template.render(context, request))
  else:
    return redirect("loginregistration:login")

# will need to replace homepage redirects with error messages
def addPlayer(request, id):
  if PlayerList.objects.filter(id=id).count() > 0:
    user = UserLoginReg.objects.get(id=request.session["user"])
    player = PlayerList.objects.get(id=id)
    if player.userid != None:
      return redirect("homepage:homepage")
    if PlayerList.objects.filter(userid=user.id, position="goalkeeper").count() > 0 and player.position == "goalkeeper":
      return redirect("homepage:homepage")
    if PlayerList.objects.filter(userid=user.id, position="defender").count() > 3 and player.position == "defender":
      return redirect("homepage:homepage")
    if PlayerList.objects.filter(userid=user.id, position="midfielder").count() > 3 and player.position == "midfielder":
      return redirect("homepage:homepage")
    if PlayerList.objects.filter(userid=user.id, position="forward").count() > 1 and player.position == "forward":
      return redirect("homepage:homepage")
    player.userid = int(request.session["user"])
    user.funds = user.funds - player.value
    if user.funds <0:
      return redirect("homepage:homepage")
    user.save()
    player.save()
    return redirect("players:players")
  else:
    return redirect("homepage:homepage")