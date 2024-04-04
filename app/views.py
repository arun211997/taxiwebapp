from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from app.models import userdata,trip,tripdata
from django.contrib import messages
from django.utils import timezone
from datetime import datetime

# Create your views here.
def mainpage(request):
    tripn=trip.objects.all()
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
        cpassword = request.POST["cpassword"]
        phone=request.POST["phone"]
        if User.objects.filter(username=username).exists():
            messages.info(request, "This username is already taken")
            return render(request , "signup.html")
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
    
def logout(request):
    auth.logout(request)
    return redirect("login")

def tripage(request):
    tripd = tripdata.objects.all()
    return render(request,"trippage.html",{'trip':tripd})

def startrip(request):
     if request.method == 'POST':
        tn = request.POST.get("trip_number")
        dn = request.POST.get("name")
        gn = request.POST.get("guest")
        fd = request.POST.get("fdate")
        sk = request.POST.get("starting_km")
        sp = request.POST.get("startplace")
        ed = request.POST.get("edate")
        ek = request.POST.get("ending_km")
        ep = request.POST.get("endplace")
        vname = request.POST.get("vehiclename")
        vnumber = request.POST.get("vnumber")
        parking = request.POST.get("parking_charge")
        if parking == "":
            parking=0
        toll = request.POST.get("toll_charge")
        if toll == "":
            parking=0
        tripkm = request.POST.get("tripkm")
        if tripkm == "":
            parking=0
        total = request.POST.get("total")
        advance = request.POST.get("advance")
        if advance == "":
            advance=0
        balance = request.POST.get("balance")
        tripcharge = request.POST.get("kilo")
        guidecharge = request.POST.get("guide")
        if guidecharge == "":
            parking=0
        hun=request.POST.get("hun")
        after=request.POST.get("after")
       
        userid= request.session['uid']
    
        data=tripdata(tripnumber=tn,drivername=dn,guestname=gn,startkm=sk,start=sp,fromdate=fd,todate=ed,
                      endkm=ek,end=ep,vehiclename=vname,vehiclenumber=vnumber,tripcharge=tripcharge,guidecharge=guidecharge,
                      parking=parking,toll=toll,tripkm=tripkm,total=total,advance=advance,balance=balance,huncharge=hun,extra=after,
                      user_id=userid,)
        data.save()
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
    return render(request,'bill.html',{'trip':tripd})

def edit(request,id):
    tripd=tripdata.objects.get(id=id)
    return render(request,'edit.html',{'trip':tripd})

def apply(request,id):
    tripd = tripdata.objects.get(id=id)
    if request.method == 'POST':
        tripd.todate = request.POST["edate"]
        tripd.end = request.POST["endplace"]
        tripd.endkm  = request.POST["ending_km"]
        tripd.parking = request.POST["parking_charge"]
        tripd.toll= request.POST["toll_charge"]
        tripd.tripkm=request.POST["tripkm"]
        tripd.total=request.POST["total"]
        tripd.advance=request.POST["advance"]
        tripd.balance=request.POST["balance"]
        tripd.tripcharge=request.POST["kilo"]
        tripd.guidecharge=request.POST["guide"]
        tripd.save()
        return render(request,'bill.html',{'trip':tripd})
