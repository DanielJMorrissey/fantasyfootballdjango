from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from loginregistration.models import UserLoginReg

"""
  need to sort out for players:
    need to find out how to import data into heroku
    will need to test that only eleven players can be added and can add different positions as long as less than 11 players
    display user league table
    create transfer in page
    sort out error messages
"""

# Create your views here.
def home(request):
  userLoggedIn = ""
  if "user" in request.session:
    userLoggedIn = UserLoginReg.objects.get(id=request.session['user'])
    if userLoggedIn:
      
      context= {
        'user' : userLoggedIn,
        'request': request.session['user']
      }
  template = loader.get_template('homepage.html')
  if userLoggedIn:
    return HttpResponse(template.render(context, request))
  else:
    return HttpResponse(template.render())