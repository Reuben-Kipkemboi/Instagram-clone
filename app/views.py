from django.shortcuts import render ,redirect 
from . forms import NewPostForm
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . models import Instagram_post, User_comment, User_likes, Profile,User


# Create your views here.
def app_home(request):
    form=NewPostForm
    images = Instagram_post.objects.all()
    users = User.objects.all()
    
    return render(request, 'index.html', {'form':form, 'images':images, 'users':users})

#Register function
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = RegisterForm()
        
        if request.method =="POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "account created for" + user )
                return redirect('login')
            
        return render(request, 'register.html', {'form':form, 'messages':messages})
    
#login function

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method =="POST":
            username= request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password = password)
            
            if user is not None:
                login(request, user)
                print('login was succesful and welcome to insta')
                return redirect('home')
            else:
                messages.info(request, "invalid credentials")
        return render(request, 'login.html', {'messages':messages})

#logout function
def user_logout(request):
	logout(request)
	return redirect('login')

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

# we will use signals to try and create profiles automatically when a user is created:
# Basic components of signals:
#---Sender: is usually a model that notifies the receiver when an event occurs.
#----Receiver: The receiver is usually a function that works on the data once it is notified of some action that has taken place for instance when a user instance is just about to be saved inside the database.
#----The connection between the senders and the receivers is done through “signal dispatchers”.

def user_profile(request):
    return render (request, 'profile.html')

def search(request):
    profiles=Profile.objects.all()
    posts=Instagram_post.objects.all()
    if 'search' in request.GET and request.GET["search"]:
        term_of_search = request.GET.get("search")
        searched_posts = Instagram_post.search_post(term_of_search)
        print("*--*--*--*--*--*--*--*--*--*--*--*--*")
        print(searched_posts)
        message = f"{term_of_search}"

        return render(request, 'search.html',{"message":message,"posts": searched_posts, 'profiles':profiles, 'posts':posts})

    else:
        message = "seems you have not provided a search input"
        return render(request, 'search.html',{"message":message})
    
