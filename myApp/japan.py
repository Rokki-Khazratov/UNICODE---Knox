from django.urls import path
from django.shortcuts import render
import base64
import hashlib 


# knox > Knox > myApp > views.py

def addSite (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        value = request.POST.get('value')
        header = request.POST.get('header')
        footer = request.POST.get('footer')

        # if username == hashlib.sha256(b"(knox.1234312131231)user").hexdigest():
        #     print("Is Users")
        # elif username == hashlib.sha256(b"(knox.1234312131231)admin").hexdigest():
        #     print("Is Administrator")
        # else:
        #     print("Is Hacker")
            

    
    context = {
        'username' : username,
        'value' : str(base64.b64decode(header), "utf-8") + value + str(base64.b64decode(footer), "utf-8"),

    }
    return render(request, 'Japan/addSite.html',context)



# knox > Knox > myApp > urls.py

class Japan () :
    patterns = [
            path('site-register', addSite, name='site-register'),
        ]
