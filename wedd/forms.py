# from django import forms
# from django.forms import ModelForm
# from .models import kumbi

# #Create a iplist form

# class kumbiForm(ModelForm):
#     class Meta:
#         model = kumbi
#         fields = ('full_name','email','password','confirmPassword','dob','gender')

#         labels = {
#             'full_name' : '',
#             'email' :'',
#             'password' : '',
#             'confirmPassword' : '',
#             'dob' :'',
#             'gender' : 'Gender',
            
#         }

#         widgets = {
            
#             # 'group' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Group'}),
#             # 'group' : forms.ChoiceField( choices=[group_choices], required=False),
#             'full_name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter your full name'}),
#             # 'site' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Site'}),
#             'email' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'email'}),
#             'password' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter your password'}),
#             'confirmPassword' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Confirm your password'}),
#             'dob' : forms.DateInput(attrs={'class' : 'form-control','placeholder' : 'Date of Birth'}),
#         }

from django import forms
from .models import MatrimonialProfile

class MatrimonialProfileForm(forms.ModelForm):
    class Meta:
        model = MatrimonialProfile
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
