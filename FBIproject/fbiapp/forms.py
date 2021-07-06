from django import forms
from .models import User

class UserSignupForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = {'user_id', 'password', 'name','age', 'keyword','state','environment','cycle' }


class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = {'user_id', 'password'}