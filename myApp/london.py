from django.urls import path
from django.shortcuts import render
import base64
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.conf import settings


# knox > Knox > myApp > views.py
def profile (request): 
    if request.COOKIES.get('cookies.authorization'):
        for usernames in User.objects.all():
            if str(usernames.id) == request.COOKIES.get('cookies.authorization'):
                data = {
                  "user" : usernames
                }
                return render(request, 'London/profile.html', data)
    else:
      return redirect(str(settings.URL_SITE) + "/register")


# knox > Knox > myApp > urls.py
class London () :
   patterns = [
      path('profile', profile, name='profile'),
    ]

