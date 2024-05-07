from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from app.models import userdata,trip,tripdata,contact,guidemod,tollcharge,othercharges,parkingcharges
from django.contrib import messages
from django.utils import timezone
from datetime import datetime

# Create your views here.
def mainpage(request):
    user=user=request.session['uid']
    tripn=trip.objects.get(user_id=user)
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
        if userdata.objects.filter(phone=phone).exists():
            messages.info(request, "This number is already taken")
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
            data2 = trip(tripnumber="TRIP001",user_id=userd)
            data2.save()
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
    user=request.session['uid']
    tripd=tripdata.objects.filter(user_id=user)
    if tripd:
         return render(request,"trippage.html",{'p':tripd})
    else:
        return render(request,"notrip.html")

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
            toll=0
        tripkm = request.POST.get("tripkm")
        if tripkm == "":
            tripkm=0
        total = request.POST.get("total")
        print(total)
        advance = request.POST.get("advance")
        if advance == "":
            advance=0
        balance = request.POST.get("balance")
        tripcharge = 0
        guidecharge = request.POST.get("guide_charge")
        if guidecharge == "":
            guidecharge=0
        othercharge = request.POST.get("other")
        if othercharge == "":
            othercharge=0
        hun=request.POST.get("hun")
        after=request.POST.get("after")
       
        userid= request.session['uid']
    
        data=tripdata(tripnumber=tn,drivername=dn,guestname=gn,startkm=sk,start=sp,fromdate=fd,todate=ed,
                      endkm=ek,end=ep,vehiclename=vname,vehiclenumber=vnumber,tripcharge=tripcharge,guidecharge=guidecharge,
                      parking=parking,toll=toll,tripkm=tripkm,total=total,advance=advance,balance=balance,huncharge=hun,extra=after,
                      user_id=userid,other = othercharge)
        data.save()
        tollch = tollcharge(tripno=tn,charge=toll,user_id=userid)
        tollch.save()

        tcount = request.POST.get("tcount")
        if tcount:
            inputcount = int(tcount)
            for x in range(1, inputcount + 1):
                toll_id = "toll_charge_" + str(x)
                tcharge = request.POST.get(toll_id)
                tolldata = tollcharge(charge=tcharge,tripno=tn,user_id=userid)
                tolldata.save()
        
        pcount = request.POST.get("pcount")
        if pcount:
            inputcount = int(pcount)
            for x in range(1, inputcount + 1):
                parking_id = "parking_charge_" + str(x)
                parking_charge = request.POST.get(parking_id)
                parkdata = parkingcharges(charge=parking_charge,tripno=tn,user_id=userid)
                parkdata.save()

        gcount = request.POST.get("count")
        if gcount == "":
            gcount = 0
        if gcount > 0:
            inputcount = int(gcount)
            for x in range(1, inputcount + 1):
                guide_id = "guide_charge_" + str(x)
                place_id = "addplace_" + str(x)
                gcharge = request.POST.get(guide_id)
                gplace = request.POST.get(place_id)
                if gcharge and gplace:
                    guidedata = guidemod(charge=gcharge, placw=gplace, tripno=tn)
                    guidedata.save()

        user=request.session['uid']
        tripn=trip.objects.get(user_id=user)
        tripnum=tripn.tripnumber
        numeric_part = int(tripnum[4:])
        numeric_part += 1
        new_trip_number = f'TRIP{numeric_part:03d}'
        tripn.tripnumber=new_trip_number
        tripn.save()
        return redirect("tripage")
        
def bill(request,id):
    tripd=tripdata.objects.get(id=id)
    tripno = tripd.tripnumber
    guide=guidemod.objects.filter(tripno=tripno)
    other =othercharges.objects.filter(tripno=tripno)
    parking =parkingcharges.objects.filter(tripno=tripno)
    toll= parkingcharges.objects.filter(tripno=tripno)
    charge = int(tripd.guidecharge)
    context = {'trip':tripd,'guide':guide ,'charge':charge,'other':other}
    return render(request,'bill.html',context)

def taxiland(request):
    return render(request,'taxiland.html')

def edit(request,id):
    tripd=tripdata.objects.get(id=id)
    userid= request.session['uid']
    tn = tripd.tripnumber
    tolld = tollcharge.objects.filter(user_id=userid ,tripno =tn)
    guide=guidemod.objects.filter(tripno=tn)
    other =othercharges.objects.filter(tripno=tn)
    parking =parkingcharges.objects.filter(tripno=tn)
    toll= tollcharge.objects.filter(tripno=tn)
    context = {'trip':tripd,'toll':tolld,'tolld':toll,'parking':parking,'other':other,'guide':guide}
    return render(request,'edit.html',context)

def review(request):
    name = request.POST["name"]
    phone = request.POST["phone"]
    review = request.POST["message"]
    data = contact(name=name, phone=phone, review = review)
    data.save()
    return redirect("taxiland")


def apply(request,id):
    tripd = tripdata.objects.get(id=id)
    if request.method == 'POST':
        tripd.todate = request.POST["edate"]
        tripd.end = request.POST["endplace"]
        tripd.endkm  = request.POST["ending_km"]
        tripd.huncharge = request.POST["hun"]
        tripd.extra = request.POST["after"]
        parking = request.POST.get("parking_charge")
       
        tripd.vehiclenumber = request.POST["vnumber"]
        if parking: 
                tripno = tripd.tripnumber
                userid= request.session['uid']
                print(parking)
                parkli = parkingcharges(tripno = tripno,user_id=userid,park=str(parking))
                parkli.save()
        else:
            tripd.parking = 0

        toll = request.POST.get("toll_charge")
        if toll:
            # extratoll = int(request.POST["totaltoll"])
            # tripd.toll = int(toll) + extratoll
            tripno = tripd.tripnumber
            userid= request.session['uid']
            tolld = tollcharge(toll=toll,tripno =tripno,user_id=userid)
            tolld.save()
        else:
            tripd.toll = 0

        other = request.POST["other"]
        if other:
            # extraother = int(request.POST["totalother"])
            # tripd.other = int(other) + extraother
            tripno = tripd.tripnumber
            userid= request.session['uid']
            otherd = othercharges(ocharge=other,tripno =tripno,user_id=userid)
            otherd.save()
        else:
            tripd.other = 0

        tripd.tripkm=request.POST["tripkm"]
        tripd.total=request.POST["total"]
        advance = request.POST["advance"]
        if advance:
            tripd.advance=request.POST["advance"]
        else:
            tripd.advance=0
        balance = request.POST["balance"]
        if balance:
            tripd.balance=request.POST["balance"]
        else:
            tripd.balance=0
        tripd.tripcharge=request.POST["kilo"]

        guide = request.POST["guide_charge"]
        guide_place = request.POST["guide_place"]
        if guide:
        #   extraguide = int(request.POST["totalguide"])
        #   tripd.guidecharge = int(guide) + extraguide
            tripno = tripd.tripnumber
            userid= request.session['uid']
            print(guide)
            print(guide_place)
            guided = guidemod(guidecharge=guide,tripno =tripno,user_id=userid,place=guide_place)
            guided.save()
        else:
            tripd.guidecharge = 0

        othercharge = request.POST["other"]
        if othercharge:
            extraother = int(request.POST["totalother"])
            tripd.other = int(othercharge) + extraother
        else:
            tripd.other = 0
            print("no")

        userid= request.session['uid']
        tcount = request.POST.get("tcount")
        print(tcount)
        if tcount:
            inputcount = int(tcount)
            for x in range(1, inputcount + 1):
                toll_id = "toll_charge_" + str(x)
                tcharge = request.POST.get(toll_id)
                tn = tripd.tripnumber
                tolldata = tollcharge(toll=tcharge,tripno=tn,user_id=userid)
                tolldata.save()
                return redirect("tripage")
            
        pcount = request.POST.get("pcount")
        print(pcount)
        if pcount:
            inputcount = int(pcount)
            for x in range(1, inputcount + 1):
                parking_id = "parking_charge_" + str(x)
                print(parking_id)
                parking_charge = request.POST.get(parking_id)
                print(parking_charge)
                tn = tripd.tripnumber
                parkdata = parkingcharges(park=parking_charge,tripno=tn,user_id=userid)
                parkdata.save()
        
        ocount = request.POST.get("ocount")
        print(ocount)
        if ocount:
            inputcount = int(ocount)
            for x in range(1, inputcount + 1):
                other_id = "other_charge_" + str(x)
                print(other_id)
                other_charge = request.POST.get(other_id)
                print(other_charge)
                tn = tripd.tripnumber
                otherdata = othercharges(ocharge=other_charge,tripno=tn,user_id=userid)
                otherdata.save()
        
        charge = request.POST.get("count")
        print(charge)
        if charge != "":
            inputcount = int(charge)
            for x in range(1, inputcount + 1):
                guide_id = "guide_charge_" + str(x)
               
                place_id = "addplace_" + str(x)
               
                gcharge = request.POST.get(guide_id)
               
                gplace = request.POST.get(place_id)
                
                tn = tripd.tripnumber
                if gcharge:
                    guidedata = guidemod(guidecharge=gcharge, place=gplace, tripno=tn , user_id =userid)
                    guidedata.save()

       
        tripno = tripd.tripnumber
        tolld = tollcharge.objects.filter(tripno = tripno)
        parkd = parkingcharges.objects.filter(tripno = tripno)
        guidedata = guidemod.objects.filter(tripno=tripno)
        otherdata = othercharges.objects.filter(tripno = tripno)
        id_list = []
        park_list = []
        guide_list =[]
        other_list =[]

        for toll in tolld:
          id_list.append(toll.id)
        for x in id_list:
          echarge = request.POST.get("toll_"+str(x))
          gett = tolld.get(id=x)
          gett.toll = echarge
          gett.save()

        for park in parkd:
            park_list.append(park.id)
        for x in park_list:
            pcharge = request.POST.get("parking_charge_"+str(x))
            getp = parkd.get(id=x)
            getp.park = pcharge
            getp.save()

        for guide in guidedata:
            guide_list.append(guide.id)
        for x in guide_list:
            gcharge = request.POST.get("guide_"+str(x))
            gplace = request.POST.get("place_"+str(x))
            getg = guidedata.get(id=x)
            getg.guidecharge = gcharge
            getg.place = gplace
            getg.save()

        for other in otherdata:
            other_list.append(other.id)
        for x in other_list:
            ocharge = request.POST.get("other_"+str(x))
            geto = otherdata.get(id=x)
            geto.ocharge = ocharge
            geto.save()
        
        tripno = tripd.tripnumber
        tolld = tollcharge.objects.filter(tripno = tripno, user_id =userid)
        parkd = parkingcharges.objects.filter(tripno = tripno, user_id =userid)
        ttotal = 0
        ptotal = 0

        # for p in tolld:
        #     tcharge = int(p.toll)
        #     ttotal+=tcharge
        # tripd.toll = ttotal
        # tripd.save()
        
        # for p in parkd:
        #     pcharge = int(p.park)
        #     ptotal+=pcharge
        # tripd.parking = ptotal
        # tripd.save()

        
        return redirect("tripage")
    
def remarks(request):
    review = contact.objects.all()
    return render(request , "review.html" ,{'review':review})
