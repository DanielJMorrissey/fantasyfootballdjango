from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from loginregistration.models import UserLoginReg
from django.contrib.auth.hashers import make_password, check_password
import re
from django.urls import reverse

# Create your views here.
def login(request):
    if "user" not in request.session:
        userLoggedIn = UserLoginReg.objects.all().values()
        template = loader.get_template('login.html')
        context= {
            'user' : userLoggedIn,
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect("homepage:homepage")

def computeLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    if len(username) == 0:
        if "errorMessage" in request.session:
            del request.session["errorMessage"]
        if "passErrorMessage" in request.session:
            del request.session["passErrorMessage"]
        usernameError = "A username is required!"
        request.session["errorMessage"] = usernameError
        return redirect("loginregistration:login")
    if len(password) == 0:
        if "errorMessage" in request.session:
            del request.session["errorMessage"]
        if "passErrorMessage" in request.session:
            del request.session["passErrorMessage"]
        passwordError = "A password is required!"
        request.session["passErrorMessage"] = passwordError
        return redirect("loginregistration:login")
    userCheck = UserLoginReg.objects.filter(username=username).count()
    if userCheck != 1:
        if "errorMessage" in request.session:
            del request.session["errorMessage"]
        if "passErrorMessage" in request.session:
            del request.session["passErrorMessage"]
        errorMessage = "Wrong Username given!"
        request.session["errorMessage"] = errorMessage
        return redirect("loginregistration:login")
    user = UserLoginReg.objects.get(username=username)
    password = make_password(password, salt="please")
    if user.username == username and user.password == password:
        if "errorMessage" in request.session:
            del request.session["errorMessage"]
        if "passErrorMessage" in request.session:
            del request.session["passErrorMessage"]
        request.session['user'] = user.id
        user.signin = True
        user.save()
        success = "Welcome User!"
        template = loader.get_template('homepage.html')
        context = {
            'success' : success,
            'user': user,
            'userSession' : request.session['user'],
        }
        return redirect('homepage:homepage')
    elif user.password != password:
        if "errorMessage" in request.session:
            del request.session["errorMessage"]
        if "passErrorMessage" in request.session:
            del request.session["passErrorMessage"]
        passErrorMessage = "Incorrect password"
        request.session["passErrorMessage"] = passErrorMessage
        return redirect("loginregistration:login")
    return redirect("loginregistration:login")



def register(request):
    if "user" not in request.session:
        userLoggedIn = UserLoginReg.objects.all().values()
        template = loader.get_template('register.html')
        context= {
            'user' : userLoggedIn,
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect("homepage:homepage")

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
        elif not re.match("^[a-zA-Z0-9-_]+@[a-zA-Z0-9.]+\.[a-z]{1,3}$", email):
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
            password = make_password(password, salt="please")
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
    user.save()
    del request.session['user']
    return redirect(reverse('loginregistration:login'))
    
