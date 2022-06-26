from tkinter import Widget
from attr import attr
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class Sign_upForm(UserCreationForm):
    mobile=forms.CharField(max_length=20,required=False)
    password2=forms.CharField(label='Conform Pasword',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    mobile=forms.CharField(error_messages={'required':'Enter Your Mobile No'},widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobile No'}))
    password1=forms.CharField(error_messages={'required':'Enter Your Correct Password'} ,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Conform Password'}))
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','mobile']
        labels={'username':"Full Name",'email':"Email Id"}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email ID'}),
            
        }
class Sign_in_Form(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password=forms.CharField(error_messages={'required':'Enter Correct Password'},widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))