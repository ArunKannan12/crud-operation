from .models import *
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter user name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'enter E-mail'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-enter password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("An user with this email already exists!")
        return email

class upload(forms.ModelForm):
    title=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control',
                                                                      'placeholder':'Please enter the name',
                                                                      'style':'width:300px;height:50px;border-radius:10px;border:2px skyblue solid;'}))
    # csvupload=forms.FileField(required=True)
    
    class Meta:
        model=csv
        fields=['title']
    
