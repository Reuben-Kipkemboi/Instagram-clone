from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Instagram_post ,User_comment, Profile

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
        
#user profile        

class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
        
     