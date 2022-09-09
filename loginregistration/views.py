from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from loginregistration.models import UserLoginReg

# Create your views here.
def login(request):
    userLoggedIn = UserLoginReg.objects.all().values()
    template = loader.get_template('login.html')
    context= {
        'user' : userLoggedIn,
    }
    return HttpResponse(template.render(context, request))

def register(request):
    userLoggedIn = UserLoginReg.objects.all().values()
    template = loader.get_template('register.html')
    context= {
        'user' : userLoggedIn,
    }
    return HttpResponse(template.render(context, request))