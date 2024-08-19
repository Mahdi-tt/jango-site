from django.shortcuts import render
from django.http import HttpResponse
def contact(request):
    return render(request,'website/contact.html')
def home(request):
    return render(request,'website/home.html')