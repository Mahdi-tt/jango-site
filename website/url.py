from django.urls import path
from website.views import index
from website.views import contact
from website.views import about
from website.views import *

app_name='website'
urlpatterns = [
    path('',index,name='index'),
    path('contact',contact,name='contact'),
    path('about',about,name='about'),
    path('Newsletter',Newsletter,name='Newsletter'),
]
