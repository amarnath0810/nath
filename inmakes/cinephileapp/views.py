from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from .models import place
from .models import persons
class HTTpResponse:
    pass


def demo(request):
    obj=place.objects.all()
    obj1=persons.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})

def register(request):
    if request.method=='POST':
        Username=request.POST['username']
        First_name=request.POST['first_name']
        Last_name = request.POST['last_name']
        Email = request.POST['email id']
        Password = request.POST['password']
        C_Password = request.POST['password1']
        if Password==C_Password:
            if User.objects.filter(username=Username).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            elif User.objects.filter(email=Email).exists():
                messages.info(request,"email already used")
                return redirect('register')

            else:
                user=User.objects.create_user(username=Username,password=Password,first_name=First_name,last_name=Last_name,email=Email)
                user.save();
                return redirect('login')
                print("user created")
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username= username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid user")
            return redirect('login')

    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})
#
