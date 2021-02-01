from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages         #for flash messages

from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
    

    return render(request,'home.html')

def registerPage(request):
    form=CreateUserForm()                         #setting form variable as function CreateUserForm

    if request.method=="POST":
        form=CreateUserForm(request.POST)         #putting value of filled CreateUserForm in form
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user)


            return redirect('loginPage')


    context={'form':form}                           #sending for as context
    return render(request,"register.html",context)



def loginPage(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password is incorrect')

    return render(request,"login.html")


def logoutuser(request):
    logout(request)
    return redirect('login')