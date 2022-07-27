from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms
from . models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name','last_name','email','messages']

class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']


class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','email','phone','address','state','pix']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'last Name'}),
            'email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email address'}),
            'phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'phone number'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'your address'}),
            'state':forms.Select(attrs={'class':'form-control', 'placeholder':'your state'}),
            'pix':forms.FileInput(attrs={'class':'form-control'})
        }
       
       
class ShopcartForm(forms.ModelForm):
    class Meta:
        model = Shopcart
        fields = ['quantity']


