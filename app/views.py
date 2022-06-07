from django.shortcuts import get_object_or_404, render ,redirect 
from . forms import NewPostForm, CommentsForm,ProfileUpdateForm
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from . models import Instagram_post, User_comment, User_likes, Profile,User, NewsLetterRecipients
from .email import send_welcome_email

# Application views here.

# @login_required(login_url='login')
def app_home(request):
    current_user = request.user
    form_one=NewPostForm
    form_two = CommentsForm
    images = Instagram_post.objects.all()
    users = User.objects.all()
    likes = User_likes.objects.all()
    comments= User_comment.objects.all()
    profiles = Profile.objects.all()
    users = User.objects.all
    return render(request, 'index.html', {'form_one':form_one, 'images':images, 'users':users, 'likes':likes, 'form_two':form_two, 'comments':comments,'profiles':profiles, 'users':users})

#Register function
# @login_required(login_url='login')
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
                email = form.cleaned_data.get('email')
                recipient = NewsLetterRecipients(user = user,email =email)
                recipient.save()
                send_welcome_email(user,email)
                messages.success(request, "account created for" + user )
                return redirect('login')
            
        return render(request, 'register.html', {'form':form, 'messages':messages})
    
#login function
# @login_required(login_url='login')
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

# @login_required(login_url='login')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
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

# @login_required(login_url='login')
def user_profile(request):
    current_user = request.user
    my_images = Instagram_post.objects.filter(user=current_user)
    print(my_images)
    return render (request, 'profile.html', {'images':my_images})


@login_required(login_url='login')
def update_profile(request):
    if request.method == 'POST':
        userprofileform = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if  userprofileform.is_valid():
            userprofileform.save()
            return redirect(to='profile')
    else:
        form_three=ProfileUpdateForm(instance =request.user.profile)
    return render(request,'update_profile.html',{'form':form_three})

# @login_required(login_url='login')
def search(request):
    profiles=Profile.objects.all()
    posts=Instagram_post.objects.all()
    if 'search' in request.GET and request.GET["search"]:
        term_of_search = request.GET.get("search")
        users = Profile.search_profiles(term_of_search)
        searched_posts = Instagram_post.search_post(term_of_search)
        print("*--*--*--*--*--*--*--*--*--*--*--*--*")
        print(searched_posts)
        message = f"{term_of_search}"

        return render(request, 'search.html',{"message":message,"posts": searched_posts, 'profiles':profiles, 'users':users})

    else:
        message = "seems you have not provided a search input"
        return render(request, 'search.html',{"message":message})
    
   

# @login_required(login_url='login')
def like_post(request, post_id):
    post = get_object_or_404(Instagram_post,id = post_id)
    #basically get_object or 404 looks for that post if it exists get the object if not return a 404.
    user_like = User_likes.objects.filter(post=post, person_liking = request.user).first()
    #checks to validate the post and user
    
    #check if there is an existing like or not
    if user_like is None:
        #if the user has not liked
        user_like=User_likes()
        user_like.post=post
        user_like.person_liking = request.user
        #save the user like by calling tha save method
        user_like.save_user_likes()
    else:
        user_like.delete_user_likes()
    #after wards
    return redirect('home')

# @login_required
# @login_required(login_url='login')
def comment(request, post_id):
    current_user = request.user
    post = Instagram_post.objects.get(id=post_id)
    user_name = User.objects.get(username=current_user.username)
    comments= User_comment.objects.all()
    
    if request.method == 'POST':
        form_four = CommentsForm(request.POST, request.FILES)
        if form_four.is_valid():
            user_comment = form_four.save(commit=False)
            user_comment.post = post
            user_comment.user = request.user
            user_comment.save()  
            return redirect('home')
    else:
        form_four = CommentsForm()
        return render(request, 'comment.html',{'form_four':form_four,'comments':comments})
    

    
