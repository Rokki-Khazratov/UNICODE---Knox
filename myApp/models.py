from django.db import models
from django.urls import reverse
from django.core import serializers
import json

   
class Users (models.Model) :
   username = models.CharField(max_length=250, unique=True)
   full_name = models.CharField(max_length=250, unique=True)
   image = models.TextField(blank=True)
   info = models.TextField(blank=True)
   number = models.CharField(max_length=50, unique=True)
   email = models.CharField(max_length=100, unique=True)
   password = models.CharField(max_length=50)
   key = models.TextField(max_length=50, unique=True, primary_key=True)
   data = models.DateField(blank=True)
   
class Tags (models.Model) :
   image = models.ImageField( upload_to = "static/tags/", null=True, blank=True)
   title = models.CharField(max_length=250)
   slug = models.SlugField(unique=True, null=True)
   paragraph = models.TextField(blank=True)

COLOR_CHOICES = ()


for i in json.loads(serializers.serialize("json", Tags.objects.all())):
   COLOR_CHOICES += (i['fields']['slug'], i['fields']['slug']),

class Components (models.Model) :
   image = models.ImageField( upload_to = "static/components/", null=True, blank=True)
   title = models.CharField(max_length=250)
   slug = models.SlugField(unique=True, null=True)
   order = models.CharField(max_length=25)
   value = models.TextField(blank=True)
   javascript = models.TextField(blank=True)
   data = models.DateField(blank=True)
   color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')

class Site (models.Model) :
   title = models.CharField(max_length=250)
   slug = models.SlugField(unique=True, null=True)
   html = models.TextField(blank=True)
   modal = models.TextField(blank=True)
   user = models.CharField(blank=True, max_length=250)

def __str__(self):
   return self.title

def get_absolute_url(self):
   return reverse('component:login', kwargs = {'slug' : self.slug})