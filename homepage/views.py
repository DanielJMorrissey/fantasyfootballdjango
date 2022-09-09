from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from loginregistration.models import UserLoginReg

"""
  need to sort out for log in and reg:
    create session
    remove record
    make only a single user can be logged in at a time
    each template gets the sign in boolean
    each view checks if logged in
    if logged in or registered, log in and reg page won't show
"""

# Create your views here.
def home(request):
  signedInUser = request.session.get('user')
  if signedInUser:
    userLoggedIn = UserLoginReg.objects.get(id=signedInUser)
    context= {
      'user' : userLoggedIn,
    }
  template = loader.get_template('homepage.html')
  if signedInUser:
    return HttpResponse(template.render(context, request))
  else:
    return HttpResponse(template.render())