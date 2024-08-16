from django.shortcuts import render
from django.http import HttpResponse
def contact(request):
    return HttpResponse ('<h1>contact Page<h1>')
def home(request):
    return HttpResponse ('<h1>Home Page<h1>')