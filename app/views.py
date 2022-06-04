from django.shortcuts import render ,redirect 
from . forms import NewPostForm
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages


# Create your views here.
def app_home(request):
    return render(request, 'index.html')

def register(request):
    form = RegisterForm()
    
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "account created for" + user )
            return redirect('login')
        
    return render(request, 'register.html', {'form':form, 'messages':messages})

def login(request):
    return render(request, 'login.html')

def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.creator = current_user
            post.save()
        return redirect('home')

    else:
        form =  NewPostForm()
    return render(request, 'post.html', {"form": form})
    
