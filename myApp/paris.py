from multiprocessing import context
from django.urls import path, reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from email import message
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
import base64
from django.contrib.auth.hashers import make_password
from . import london
from django.conf import settings


# knox > Knox > myApp > views.py

# register

def register (request):   
    if request.COOKIES.get('cookies.authorization'):
        for usernames in User.objects.all():
            if str(usernames.id) == request.COOKIES.get('cookies.authorization'):
                return redirect(str(settings.URL_SITE) + "/profile")
                # return london.profile(request)
    else:
        if request.method == 'POST' :
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            repassword = request.POST['repassword']

            for usernames in User.objects.all():
                if usernames.username == username:
                    return redirect('knox:register')
                else:
                    if password == repassword:
                        if username == "" or len(username) < 3:
                            return redirect('knox:register')
                        elif 8 >= len(password) >= 255:
                            return redirect('knox:profile')
                        else:
                            user = User.objects.create_user (username=username, email=email,password=password) 
                            context = {
                                "user" : user
                            }
                            response = redirect(str(settings.URL_SITE) + "/profile") 
                            response.set_cookie('cookies.authorization', str(user.id))
                            
                            user.save()
                            return response
                            
                            
        else:   
            return render (request, 'Paris/register.html')


# login

def login(request):
    if request.COOKIES.get('cookies.authorization'):
        for usernames in User.objects.all():
            if str(usernames.id) == request.COOKIES.get('cookies.authorization'):
                return redirect(str(settings.URL_SITE) + "/profile")
                # return london.profile(request)
    else:
        context = {"response" : "Hello Start signings"}
        if request.method == "POST":
            username_login = request.POST['username']
            for usernames in User.objects.all():
                access = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
                if access != None:
                    context = {
                        "user" : usernames
                    }
                    response = redirect(str(settings.URL_SITE) + "/profile") 
                    print("$"*50)
                    print(access.id)          
                    response.set_cookie('cookies.authorization', str(access.id))
                    return response
                else:
                    context = {
                        "response" : "Password or Username not correct"
                    }
                    response = render(request, 'Paris/login.html', context)        
                    return response

        response = render(request, 'Paris/login.html', context)
        return response
 
# knox > Knox > myApp > urls.py

class Paris ():
    patterns = [
      path('register/',register, name='register'),
      path('login/',login, name='login'),
    ]