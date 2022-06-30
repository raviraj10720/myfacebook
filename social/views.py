from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        if request.method=='POST':
            username = request.POST['username']
            pwd = request.POST['password']
            user = authenticate(username=username,password=pwd)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        return redirect('home')

    return render(request,'index.html')
@login_required(login_url='index')

def home (request):
    user = request.user
    context = {'user':user}
    return render(request,'home.html',context)
    
    
@login_required(login_url='index')
def profile (request):
    user = request.user
    context = {'user':user}
    return render(request,'profile.html',context)



def signout(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        pwd = request.POST['password']
        user = User.objects.create(username=username)
        user.set_password(pwd)
        user.save()
        return redirect('index')
    return redirect ('index')