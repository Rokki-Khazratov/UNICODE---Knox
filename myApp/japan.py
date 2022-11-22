from django.urls import path
from django.shortcuts import render
import base64
import hashlib 
from .models import Site
from django.contrib.auth.models import User, auth
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.shortcuts import redirect

# knox > Knox > myApp > views.py

def addSite (request): 
    if request.method == 'POST':
        value = request.POST.get('value')
        footer = request.POST.get('footer')
        modal = request.POST.get('modal')

        if User.objects.get(id = int(request.COOKIES.get('cookies.authorization'))):
            user = User.objects.get(id = int(request.COOKIES.get('cookies.authorization')))

            try: 
                siteUser = Site.objects.get(title = user.username)
                siteUser.html = value
                siteUser.modal = modal
                siteUser.save()
            except ObjectDoesNotExist:
                newSite = Site.objects.create(title=user.username, slug=user.username, html = value, user = user.username, modal = modal)

            context = {
                'value' : value,
                'modal' : modal,
            }
            return redirect(str(settings.URL_SITE)+ '/')
        else:
            return redirect(str(settings.URL_SITE) + '/login')
    else:
        return redirect(str(settings.URL_SITE))




# knox > Knox > myApp > urls.py

class Japan () :
    patterns = [
            path('site-register', addSite, name='site-register'),
        ]
