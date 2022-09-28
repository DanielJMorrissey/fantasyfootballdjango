from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from loginregistration.models import UserLoginReg

"""
  need to sort out for log in and reg:
    probably sorted out image bug by using redirect
    need to check if there is a user in db and session
    debug login and log out
    make only a single user can be logged in at a time
    each view checks if logged in
    if logged in or registered, log in and reg page won't show
"""

# Create your views here.
def home(request):
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