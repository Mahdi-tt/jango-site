from django import forms
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth.models import User
from django.forms import EmailField
from django.utils.translation import gettext_lazy as _


class customcreatuserform(UserCreationForm):
    email = EmailField(label=_("Email address"), required=True,
    help_text=_("Required."))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2') 
