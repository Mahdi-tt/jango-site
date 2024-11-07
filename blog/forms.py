from django import forms
from django.forms import ModelForm
from blog.models import comment

class commentforms(forms.ModelForm):
     
     class Meta:
         model = comment
         exclude = ('approved',)