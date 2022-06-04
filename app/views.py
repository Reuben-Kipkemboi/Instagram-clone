from django.shortcuts import render ,redirect 
from . forms import NewPostForm


# Create your views here.
def app_home(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

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
    
