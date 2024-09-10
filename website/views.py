from django.shortcuts import render
from django.http import HttpResponse
def contact(request):
    return render(request,'website/contact.html')
def index(request):
    return render(request,'website/index.html')
def about(request):
    return render(request,'website/about.html')