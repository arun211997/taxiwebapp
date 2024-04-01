from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from app.models import userdata
from django.contrib import messages

# Create your views here.
def mainpage(request):
    return render (request, "mainpage.html")

def signup(request):
    return render (request,"signup.html")

def login(request):
    return render (request,"login.html")

def signupfunct(request):
     if request.method == "POST":
        first_name = request.POST["fname"]
        last_name = request.POST['lname']
        username = request.POST['username']
        phone=request.POST["phone"]
        password=request.POST["password"]
        phone=request.POST["phone"]
        if User.objects.filter(username=username).exists():
            messages.info(request, "This username is already taken")
            return redirect("login")
        else:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
            )
            user.save()
            userd=user.id
            data=userdata(phone=phone,user_id=userd)
            data.save()
            return redirect("login")
        
def log(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # it means that there is a valid user, and the code block within the if block will be executed.
            auth.login(request,user)
            request.session['uid']=user.id
            return redirect("mainpage")
        else:
            messages.info(request, "Invalid password or Password")
            return redirect("login")
    else:
        return redirect("login")
    
def logout(request):
    auth.logout(request)
    return redirect("login")