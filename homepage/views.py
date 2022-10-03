from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from loginregistration.models import UserLoginReg

"""
  need to sort out for log in and reg:
    improve validation - JavaScript and python
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