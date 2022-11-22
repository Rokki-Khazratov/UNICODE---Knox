from multiprocessing import context
from django.urls import path, reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from email import message
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
import base64
from django.contrib.auth.hashers import make_password
from . import london
from django.conf import settings
from .models import Site


# knox > Knox > myApp > views.py 

# views

def view (request, post_slug = None):
    print("="*100)
    # if request.COOKIES.get('cookies.authorization'):
    for site in Site.objects.all():
        search = request.POST.get('search', False)
        if str(site.title) == search:
            context = {
                'site' : site
            }
            return render (request, 'Paris/view.html', context)
        elif  str(site.title) == str(post_slug):
            context = {
                'site' : site
            }
            return render (request, 'Paris/view.html', context)
    else:
        context = {
            'site' : Site.objects.get(title = "four04")
        }
        return render (request, 'Paris/view.html', context)


    


# register

def register (request):
    print("="*100)
    context = {"response" : "Hello Start signings"}   
    if request.COOKIES.get('cookies.authorization'):
        print("="*100)
        for usernames in User.objects.all():
            if str(usernames.id) == request.COOKIES.get('cookies.authorization'):
                return redirect(str(settings.URL_SITE) + "/profile")
                # return london.profile(request)
    elif request.method == 'POST' :
        print("="*100)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        for usernames in User.objects.all():
            if usernames.username == username:
                return redirect(str(settings.URL_SITE) + "/register")
            else:
                if password == repassword:
                    if username == "" or len(username) < 3:
                        return redirect(str(settings.URL_SITE) + "/register")
                    elif 8 >= len(password) >= 255:
                        return redirect(str(settings.URL_SITE) + "/register")
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
            return render (request, 'Paris/register.html', context) 
    
    print("="*100)
    return render (request, 'Paris/register.html', context)


# login

def login(request):
    context = {"response" : "Hello Start signings"}
    if request.COOKIES.get('cookies.authorization'):
        for usernames in User.objects.all():
            if str(usernames.id) == request.COOKIES.get('cookies.authorization'):
                return redirect(str(settings.URL_SITE) + "/profile")
                # return london.profile(request)
    else:
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
                    return redirect(str(settings.URL_SITE) + "/login")        
                    return response
    return render (request, 'Paris/login.html', context)
 
# knox > Knox > myApp > urls.py

class Paris ():
    patterns = [
      path('register',register, name='register'),
      path('login',login, name='login'),
      path('<slug:post_slug>',view, name='view'),
    ]
