from django import forms
from django.forms import ModelForm
from .models import wandekar

#Create a iplist form

class wandekarForm(ModelForm):
    class Meta:
        model = wandekar
        fields = ('user_name','email','password','date_of_birth','gender')

        labels = {
            'user_name' : 'fullname',
            'email' :'email',
            'password' : 'password',
            'date_of_birth' :'date_of_birth',
            'gender' : 'gender',
            
        }