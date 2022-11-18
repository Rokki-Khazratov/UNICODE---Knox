from django.shortcuts import render
from multiprocessing import context
from .models import Components,Users,Tags
import hashlib 
from django.core import serializers


def index (request):
    # to json format for compatibility --------------------------------
    component = Components.objects.all()
    user = Users.objects.all()
    tag = Tags.objects.all()
    tagJson = serializers.serialize("json", Tags.objects.all())
    componentJson = serializers.serialize("json", Components.objects.all())

    context = {
        'component' : component,
        'user' : user,
        'tag' : tag,
        'userole' : hashlib.sha256(b"(knox.1234312131231)user").hexdigest(),
        'tagJson' : tagJson,
        'componentJson' : componentJson,
    }

    return render(request, 'Japan/index.html',context)
