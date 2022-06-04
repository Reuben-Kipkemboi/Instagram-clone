from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Instagram_post ,User_comment

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = [
            
            'email',
            'username',
            'password1',
            'password2',
        ]
        
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Instagram_post
        exclude = ['creator', 'date_posted', 'profile_of_creator']
        
     