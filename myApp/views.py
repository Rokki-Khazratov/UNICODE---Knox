
from django.shortcuts import render, redirect
from multiprocessing import context
from .models import Components,Users,Tags
import hashlib 
from django.core import serializers
from .models import Site
from django.contrib.auth.models import User, auth
from django.core.exceptions import ObjectDoesNotExist
from . import paris
from django.conf import settings


def index (request):
    if request.COOKIES.get('cookies.authorization'):
        if User.objects.get(id = int(request.COOKIES.get('cookies.authorization'))):
            user = User.objects.get(id = int(request.COOKIES.get('cookies.authorization')))

            # to json format for compatibility --------------------------------
            component = Components.objects.all()
            tag = Tags.objects.all()
            tagJson = serializers.serialize("json", Tags.objects.all())
            componentJson = serializers.serialize("json", Components.objects.all())

            try: 
                defHtml = Site.objects.get(title = user.username)

                context = {
                    'component' : component,
                    'user' : user,
                    'tag' : tag,
                    'tagJson' : tagJson,
                    'componentJson' : componentJson,
                    'defHtml' : defHtml.html,
                    'modal' : defHtml.modal,
                }
            except ObjectDoesNotExist:
                context = {
                    'component' : component,
                    'user' : user,
                    'tag' : tag,
                    'tagJson' : tagJson,
                    'componentJson' : componentJson,
                    'defHtml' : """<div ondrop="drop(event,this)" ondragover="allowDrop(event)" id="dropper" >
                        <div class="px-5 py-5 text-center">
                            <div class="px-2 py-3 rounded-4 border-3 border-primary" style="border-style: dashed;">
                            <img class="d-block mx-auto mb-4" src="https://getbootstrap.com/docs/5.2/assets/brand/bootstrap-logo.svg" alt="" width="72" height="57" />
                            <h1 class="display-10 fw-bold">Drop here</h1>
                            <div class="col-lg-11 mx-auto">
                                <p class="h6 mb-4">Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit, featuring Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful JavaScript plugins.</p>
                                <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
                                <button type="button" class="btn btn-primary px-4 gap-3">Primary button</button>
                                <button type="button" class="btn btn-outline-secondary px-4">Secondary</button>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>"""
                }

        return render(request, 'Japan/index.html',context)
    else:
        return redirect(str(settings.URL_SITE) + "/register")

def view(request, post_slug):
    return paris.view(request, post_slug)



