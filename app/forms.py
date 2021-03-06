from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Instagram_post ,User_comment, Profile



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control',}))
                                                              
    username = forms.CharField(max_length=100,required=True,
    widget=forms.TextInput(attrs={'placeholder': 'Provide your Username','class':'form-control', }))
                                                     
    password1 = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control','data-toggle': 'password', 'id':'password',})) 
                                                                         
    password2 = forms.CharField(max_length=50,required=True,
    widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control','data-toggle': 'password','id': 'password',}))
    
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
        exclude = ['user', 'date_posted', 'profile_of_creator']
        
#update user profile via the profile update form       
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['date_joined']


class CommentsForm(forms.ModelForm):
     class Meta:
        model = User_comment
        exclude = ['user', 'post']
    
        
     