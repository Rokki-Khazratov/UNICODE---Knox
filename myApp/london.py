from django.urls import path
from django.shortcuts import render
import base64
from django.contrib.auth.models import User


# knox > Knox > myApp > views.py
def profile (request):
    if request.COOKIES.get('cookies.authorization'):
        for usernames in User.objects.all():
            if str(usernames.id) == request.COOKIES.get('cookies.authorization'):
                data = {
                  "user" : usernames
                }
                return render(request, 'London/profile.html', data)


# knox > Knox > myApp > urls.py
class London () :
   patterns = [
      path('profile', profile, name='profile'),
    ]

