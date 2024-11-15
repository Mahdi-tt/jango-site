from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from accounts.forms import customcreatuserform
from django.contrib.auth.models import User

# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            # form = AuthenticationForm(request=request, data=request.POST)  
            # if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password') 
                if '@' in username:
                    user_obj = User.objects.filter(email = username).first()
                else:
                    user_obj = User.objects.filter(username = username).first()       
                if user_obj:
                    user = authenticate(request, username=user_obj.username, password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(request,'SUCCESS to login')
                        return redirect('/')
                    else:
                        messages.error(request,'errore to password')
                else:
                    messages.error(request,'errore to user name ')
    else:
        messages.error(request,'you are login')
        return redirect('/')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request,'Accounts/login.html',context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = customcreatuserform(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'success creat user')
                return redirect('/accounts/login')
            else:
                messages.error(request,form.errors.as_text())
    else:
        messages.error(request,'you are login')
        return redirect('/')        
    form = customcreatuserform()
    context = {'form':form} 
    return render(request,'Accounts/signup.html',context)