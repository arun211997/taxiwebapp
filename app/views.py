from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from app.models import userdata,trip,tripdata
from django.contrib import messages
from django.utils import timezone
from datetime import datetime

# Create your views here.
def mainpage(request):
    tripn=trip.objects.get(id=1)
    return render (request, "mainpage.html",{'trip':tripn})

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
            tripn=trip.objects.get(id=1)
            return render( request ,"mainpage.html",{'trip':tripn})
        else:
            messages.info(request, "Invalid password or Password")
            return redirect("login")
    else:
        return redirect("login")
    
def logout(request):
    auth.logout(request)
    return redirect("login")

def tripage(request):
    tripd = tripdata.objects.all()
    return render(request,"trippage.html",{'trip':tripd})

def startrip(request):
     if request.method == 'POST':
        tn=request.POST["trip_number"]
        dn=request.POST["name"]
        gn=request.POST["guest"]
        fd=request.POST["fdate"]
        sk=request.POST["starting_km"]
        sp=request.POST["startplace"]
        ed=request.POST["edate"]
        ek=request.POST["ending_km"]
        ep=request.POST["endplace"]
        vname=request.POST["vehiclename"]
        vnumber=request.POST["vnumber"]
        parking=request.POST["parking_charge"]
        toll=request.POST["toll_charge"]
        tripkm=request.POST["tripkm"]
        total=request.POST["total"]
        advance=request.POST["advance"]
        balance=request.POST["balance"]
        fixed=100
        extra=15
        userid= request.session['uid']
    
        dataf=tripdata(tripnumber=tn,drivername=dn,guestname=gn,startkm=sk,start=sp,fromdate=fd,todate=ed,
                      endkm=ek,end=ep,vehiclename=vname,vehiclenumber=vnumber,
                      parking=parking,toll=toll,tripkm=tripkm,total=total,advance=advance,balance=balance,
                      fixed=fixed,extra=extra,user_id=userid)
        dataf.save()
        tripn=trip.objects.get(id=1)
        tripnum=tripn.tripnumber
        numeric_part = int(tripnum[4:])
        numeric_part += 1
        new_trip_number = f'TRIP{numeric_part:03d}'
        tripn.tripnumber=new_trip_number
        tripn.save()
        return redirect("tripage")
     
def bill(request,id):
    tripd=tripdata.objects.get(id=id)
    return render(request,'bill.html',{'trip':'tripd'})

def edit(request,id):
    tripd=tripdata.objects.get(id=id)
    return render(request,'edit.html',{'trip':tripd})