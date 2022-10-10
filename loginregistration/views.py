from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from loginregistration.models import UserLoginReg
from django.contrib.auth.hashers import make_password, check_password
import re
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail


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
    username = username.strip()
    password = request.POST['password']
    if len(username) == 0:
        if "errorMessage" in request.session:
            del request.session["errorMessage"]
        if "passErrorMessage" in request.session:
            del request.session["passErrorMessage"]
        usernameError = "A username is required!"
        request.session["errorMessage"] = usernameError
        request.session.set_expiry(300)
        return redirect("loginregistration:login")
    if len(password) == 0:
        if "errorMessage" in request.session:
            del request.session["errorMessage"]
        if "passErrorMessage" in request.session:
            del request.session["passErrorMessage"]
        passwordError = "A password is required!"
        request.session["passErrorMessage"] = passwordError
        request.session.set_expiry(300)
        return redirect("loginregistration:login")
    userCheck = UserLoginReg.objects.filter(username=username).count()
    if userCheck != 1:
        if "errorMessage" in request.session:
            del request.session["errorMessage"]
        if "passErrorMessage" in request.session:
            del request.session["passErrorMessage"]
        errorMessage = "Wrong Username given!"
        request.session["errorMessage"] = errorMessage
        request.session.set_expiry(300)
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
        request.session.set_expiry(None)
        return redirect('homepage:homepage')
    elif user.password != password:
        if "errorMessage" in request.session:
            del request.session["errorMessage"]
        if "passErrorMessage" in request.session:
            del request.session["passErrorMessage"]
        passErrorMessage = "Incorrect password"
        request.session["passErrorMessage"] = passErrorMessage
        request.session.set_expiry(300)
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
    username = username.strip()
    teamName = request.POST['teamname']
    password = request.POST['password']
    confirmPassword = request.POST['passwordconfirm']
    email = request.POST['email']
    if len(username) == 0 or len(teamName) == 0 or len(password) == 0 or len(confirmPassword) == 0 or len(email) == 0:
        errorMessage = "A field is missing"
        if "regErrorMessage" in request.session:
            del request.session["regErrorMessage"]
        request.session["regErrorMessage"] = errorMessage
        request.session.set_expiry(300)
        return redirect("loginregistration:register")
    else:
        if len(password) < 7:
            errorMessage = "Password must be at least 7 charcters long"
            if "regErrorMessage" in request.session:
                del request.session["regErrorMessage"]
            request.session["regErrorMessage"] = errorMessage
            request.session.set_expiry(300)
            return redirect("loginregistration:register")
        elif re.search("[0-9]", password) == None:
            errorMessage = "Password must contain at least one number"
            if "regErrorMessage" in request.session:
                del request.session["regErrorMessage"]
            request.session["regErrorMessage"] = errorMessage
            request.session.set_expiry(300)
            return redirect("loginregistration:register")
        elif re.search("[A-Z]", password) == None:
            errorMessage = "Password must contain at least 1 upper case letter"
            if "regErrorMessage" in request.session:
                del request.session["regErrorMessage"]
            request.session["regErrorMessage"] = errorMessage
            request.session.set_expiry(300)
            return redirect("loginregistration:register")
        elif re.search("[a-z]", password) == None:
            errorMessage = "Password must contain at least 1 lower case letter"
            if "regErrorMessage" in request.session:
                del request.session["regErrorMessage"]
            request.session["regErrorMessage"] = errorMessage
            request.session.set_expiry(300)
            return redirect("loginregistration:register")
        elif password != confirmPassword:
            errorMessage = "Passwords do not match"
            if "regErrorMessage" in request.session:
                del request.session["regErrorMessage"]
            request.session["regErrorMessage"] = errorMessage
            request.session.set_expiry(300)
            return redirect("loginregistration:register")
        elif not re.match("^[a-zA-Z0-9-_]+@[a-zA-Z0-9.]+\.[a-z]{1,3}$", email):
            errorMessage = "Email is not in the correct format"
            if "regErrorMessage" in request.session:
                del request.session["regErrorMessage"]
            request.session["regErrorMessage"] = errorMessage
            request.session.set_expiry(300)
            return redirect("loginregistration:register")
        else:
            possibleUser = UserLoginReg.objects.filter(username=username).count()
            if possibleUser > 0:
                errorMessage = "That username is taken"
                if "regErrorMessage" in request.session:
                    del request.session["regErrorMessage"]
                request.session["regErrorMessage"] = errorMessage
                request.session.set_expiry(300)
                return redirect("loginregistration:register")
            possibleUser = UserLoginReg.objects.filter(teamname=teamName).count()
            if possibleUser > 0:
                errorMessage = "That team name is taken"
                if "regErrorMessage" in request.session:
                    del request.session["regErrorMessage"]
                request.session["regErrorMessage"] = errorMessage
                request.session.set_expiry(300)
                return redirect("loginregistration:register")
            possibleUser = UserLoginReg.objects.filter(email=email).count()
            if possibleUser > 0:
                errorMessage = "That email is taken"
                if "regErrorMessage" in request.session:
                    del request.session["regErrorMessage"]
                request.session["regErrorMessage"] = errorMessage
                request.session.set_expiry(300)
                return redirect("loginregistration:register")
            password = make_password(password, salt="please")
            newUser = UserLoginReg(username=username, email=email, signin=True, password=password, funds=100000000, score=0, teamname=teamName)
            newUser.save()
            if "regErrorMessage" in request.session:
                del request.session["regErrorMessage"]
            request.session.set_expiry(None)
            request.session['user'] = newUser.id
            subject = "Welcome to Fantasy football my friend!"
            message = f"Hello {username}, thanks for registering with fantasy football!"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ["danieljohnmorrissey@hotmail.com", ]
            send_mail( subject, message, email_from, recipient_list, fail_silently=False )
            return redirect('homepage:homepage')

def signout(request):
    user = UserLoginReg.objects.get(id=request.session['user'])
    user.signin = False
    user.save()
    del request.session['user']
    return redirect(reverse('loginregistration:login'))
    
