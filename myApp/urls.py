from .japan import Japan
from .paris import Paris
from .london import London
from django.urls import path
from . import views

app_name = "knox"
urlpatterns = [
    path('',views.index, name='index'),
] 

urlpatterns += Japan.patterns 
urlpatterns += London.patterns 
urlpatterns += Paris.patterns 