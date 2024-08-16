from django.urls import path
from website.views import home
from website.views import contact

urlpatterns = [
    path('',home),
    path('contact',contact)
]
