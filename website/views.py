from django.shortcuts import render
from django.http import *
from .forms import *
from .models import contact
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        form = contactforms(request.POST)
        if form.is_valid():
            contacts=form.save(commit=False)
            contacts.name= 'unknown'
            contacts.save()
            messages.success(request,'success ticket ')
        else:
            messages.error(request,'error ticket')
    form=contactforms()
    return render(request,'website/contact.html',{'form':form})

def index(request):
    return render(request,'website/index.html')
def about(request):
    return render(request,'website/about.html')

def Newsletter(request):
    if request.method == 'POST':
        form=Newsletterforms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'success email')
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')