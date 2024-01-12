from django import forms
from django.forms import ModelForm
from .models import wandekar

#Create a iplist form

class wandekarForm(ModelForm):
    class Meta:
        model = wandekar
        fields = ('full_name','email','password','confirmPassword','dob','gender')

        labels = {
            'full_name' : '',
            'email' :'',
            'password' : '',
            'confirmPassword' : '',
            'dob' :'',
            'gender' : 'Gender',
            
        }

        widgets = {
            
            # 'group' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Group'}),
            # 'group' : forms.ChoiceField( choices=[group_choices], required=False),
            'full_name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter your full name'}),
            # 'site' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Site'}),
            'email' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter your email'}),
            'password' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter your password'}),
            'confirmPassword' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Confirm your password'}),
            'dob' : forms.DateInput(attrs={'class' : 'form-control','placeholder' : 'Date of Birth'}),
        }