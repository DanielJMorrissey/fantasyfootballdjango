from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from loginregistration.models import UserLoginReg

# Create your views here.
def players(request):
  userLoggedIn = ""
  if "user" in request.session:
    userLoggedIn = UserLoginReg.objects.get(id=request.session['user'])
    if userLoggedIn:
      
      context= {
        'user' : userLoggedIn,
        'request': request.session['user']
      }
    template = loader.get_template('players.html')
    if userLoggedIn:
      return HttpResponse(template.render(context, request))
  else:
    return redirect("loginregistration:login")