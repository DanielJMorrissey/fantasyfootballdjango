from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from loginregistration.models import UserLoginReg
from django.contrib.auth.hashers import make_password
import re
from django.urls import reverse

# Create your views here.
def login(request):
    userLoggedIn = UserLoginReg.objects.all().values()
    template = loader.get_template('login.html')
    context= {
        'user' : userLoggedIn,
    }
    return HttpResponse(template.render(context, request))

def computeLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    userLoggedIn = UserLoginReg.objects.all().values()
    if len(username) == 0:
        # will need to add error message in template
        usernameError = "A username is required!"
        template = loader.get_template('login.html')
        context = {
            'user' : userLoggedIn,
            'usernameError' : usernameError
        }
        return HttpResponse(template.render(context, request))
    if len(password) == 0:
        # will need to add error message in template
        passwordError = "A password is required!"
        template = loader.get_template('login.html')
        context = {
            'passwordError' : passwordError
        }
        return HttpResponse(template.render(context, request))
    user = UserLoginReg.objects.get(username=username)
    password = make_password(password)
    if user.username == username and user.password == password:
        request.session['user'] = user.id
        user.signin = True
        success = "Welcome User!"
        template = loader.get_template('homepage.html')
        context = {
            'success' : success,
            'user': user,
            'userSession' : request.session['user'],
        }
        return HttpResponse(template.render(context, request))



def register(request):
    userLoggedIn = UserLoginReg.objects.all().values()
    template = loader.get_template('register.html')
    context= {
        'user' : userLoggedIn,
    }
    return HttpResponse(template.render(context, request))

def computeregistration(request):
    username = request.POST['username']
    teamName = request.POST['teamname']
    password = request.POST['password']
    confirmPassword = request.POST['passwordconfirm']
    email = request.POST['email']
    if len(username) == 0 or len(teamName) == 0 or len(password) == 0 or len(confirmPassword) == 0 or len(email) == 0:
        errorMessage = "A field is missing"
        template = loader.get_template('register.html')
        context = {
            'errorMessage' : errorMessage
        }
        return HttpResponse(template.render(context, request))
    else:
        if password != confirmPassword:
            errorMessage = "Passwords do not match"
            template = loader.get_template('register.html')
            context = {
                'errorMessage' : errorMessage
            }
            return HttpResponse(template.render(context, request))
        elif not re.match("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$", email):
            errorMessage = "Email is not in the correct format"
            template = loader.get_template('register.html')
            context = {
                'errorMessage' : errorMessage
            }
            return HttpResponse(template.render(context, request))
        else:
            possibleUser = UserLoginReg.objects.filter(username=username).count()
            if possibleUser > 0:
                errorMessage = "That username is taken"
                template = loader.get_template('register.html')
                context = {
                    'errorMessage' : errorMessage
                }
                return HttpResponse(template.render(context, request))
            possibleUser = UserLoginReg.objects.filter(teamname=teamName).count()
            if possibleUser > 0:
                errorMessage = "That team name is taken"
                template = loader.get_template('register.html')
                context = {
                    'errorMessage' : errorMessage
                }
                return HttpResponse(template.render(context, request))
            possibleUser = UserLoginReg.objects.filter(email=email).count()
            if possibleUser > 0:
                errorMessage = "That email is taken"
                template = loader.get_template('register.html')
                context = {
                    'errorMessage' : errorMessage
                }
                return HttpResponse(template.render(context, request))
            password = make_password(password)
            newUser = UserLoginReg(username=username, email=email, signin=True, password=password, funds=100000000, score=0, teamname=teamName)
            newUser.save()
            request.session['user'] = newUser.id
            success = "Welcome new User!"
            template = loader.get_template('homepage.html')
            context = {
                'success' : success,
                'user': newUser,
                'userSession' : request.session['user'],
            }
            return redirect('homepage:homepage')

def signout(request):
    user = UserLoginReg.objects.get(id=request.session['user'])
    user.signin = False
    request.session['user'] = False
    return HttpResponseRedirect(reverse('login'))
    
