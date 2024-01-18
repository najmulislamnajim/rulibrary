from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from . forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.
def register(request):
    form=UserRegistrationForm
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
    
    return render(request,'register.html',{'form':form})

def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            user=authenticate(username=username,password=password)
            if user is None:
                messages.error(request,'Invalid Password')
                return redirect('login')
            else:
                login(request,user)
                return redirect('home')
        else:
            messages.error(request,'Invalid Username')
            return redirect('login')
    return render(request,'signin.html')

def userlogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return redirect('login')
    
def not_a_member(request):
    return render(request,'message.html')

def profile(request):
    return render(request,'profile.html')