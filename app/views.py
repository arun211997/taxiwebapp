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

        totalpark = request.POST["totalpark"]
        totaltoll = request.POST.get("totaltoll")
        totalguide = request.POST.get("totalguide")
        totalother = request.POST.get("totalother")
       
        parkingc = request.POST.get("parking_charge")
        if parkingc: 
                tripno = tn
                userid= request.session['uid']
                print(parkingc)
                pchange = parkingcharges(tripno = tripno,user_id = userid,park = parkingc)
                pchange.save()

        toll = request.POST.get("toll_charge")
        if toll:
            tripno = tn
            userid= request.session['uid']
            tolld = tollcharge(toll=toll,tripno =tripno,user_id=userid)
            tolld.save()

        guide = request.POST["guide_charge"]
        guide_place = request.POST["guide_place"]
        if guide:
            tripno = tn
            userid= request.session['uid']
            guided = guidemod(guidecharge=guide,tripno =tripno,user_id=userid,place=guide_place)
            guided.save()

        other = request.POST.get("other")
        if other:
            tripno = tn
            userid= request.session['uid']
            otherd = othercharges(ocharge=other,tripno =tripno,user_id=userid)
            otherd.save()

        tripkm = request.POST.get("tripkm")
        if tripkm == "":
            tripkm=0
        total = request.POST.get("total")
        advance = request.POST.get("advance")

        if advance == "":
            advance=0
        balance = request.POST.get("balance")
        tripcharge = 0
        hun=request.POST.get("hun")
        after=request.POST.get("after")
        userid= request.session['uid']

        tcount = request.POST.get("tcount")
        if tcount:
            inputcount = int(tcount)
            for x in range(1, inputcount + 1):
                toll_id = "toll_charge_" + str(x)
                tcharge = request.POST.get(toll_id)
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
                parking = request.POST[parking_id]
                parkdata = parkingcharges(park=parking,tripno=tn,user_id=userid)
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
                if gcharge:
                    guidedata = guidemod(guidecharge=gcharge, place=gplace, tripno=tn , user_id =userid)
                    guidedata.save()
    
        data=tripdata(tripnumber=tn,drivername=dn,guestname=gn,startkm=sk,start=sp,fromdate=fd,todate=ed,
                      endkm=ek,end=ep,vehiclename=vname,vehiclenumber=vnumber,tripcharge=tripcharge,guidecharge=totalguide,
                      parking=totalpark,toll=totaltoll,tripkm=tripkm,total=total,advance=advance,balance=balance,huncharge=hun,extra=after,
                      user_id=userid, other=totalother)
        data.save()
        
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
    userid= request.session['uid']
    tripd=tripdata.objects.get(id=id)
    tripno = tripd.tripnumber
    guide=guidemod.objects.filter(tripno=tripno, user_id=userid)
    other =othercharges.objects.filter(tripno=tripno, user_id=userid)
    parking =parkingcharges.objects.filter(tripno=tripno, user_id=userid)
    toll= parkingcharges.objects.filter(tripno=tripno, user_id=userid)
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
    guide=guidemod.objects.filter(tripno=tn, user_id =userid)
    other =othercharges.objects.filter(tripno=tn, user_id =userid)
    parking =parkingcharges.objects.filter(tripno=tn, user_id =userid)
    toll= tollcharge.objects.filter(tripno=tn, user_id =userid)
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
        parkingc = request.POST.get("parking_charge")
        totalpark = request.POST["totalpark"]
        tripd.parking = totalpark
        totaltoll = request.POST.get("totaltoll")
        tripd.toll = totaltoll
        totalguide = request.POST.get("totalguide")
        tripd.guidecharge = totalguide
        totalother = request.POST.get("totalother")
        tripd.other = totalother
        tripd.vehiclenumber = request.POST["vnumber"]
        parkingc = request.POST.get("parking_charge")
        if parkingc: 
                tripno = tripd.tripnumber
                userid= request.session['uid']
                print(parkingc)
                pchange = parkingcharges(tripno = tripno,user_id = userid,park = parkingc)
                pchange.save()
        

        toll = request.POST.get("toll_charge")
        if toll:
            tripno = tripd.tripnumber
            userid= request.session['uid']
            tolld = tollcharge(toll=toll,tripno =tripno,user_id=userid)
            tolld.save()

        guide = request.POST["guide_charge"]
        guide_place = request.POST["guide_place"]
        if guide:
            tripno = tripd.tripnumber
            userid= request.session['uid']
            guided = guidemod(guidecharge=guide,tripno =tripno,user_id=userid,place=guide_place)
            guided.save()

        other = request.POST.get("other")
        print(other)
        if other:
            tripno = tripd.tripnumber
            userid= request.session['uid']
            otherd = othercharges(ocharge=other,tripno =tripno,user_id=userid)
            otherd.save()

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
       
        tripd.save()
       
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
                parking = request.POST[parking_id]
                
                tn = tripd.tripnumber
                parkdata = parkingcharges(park=parking,tripno=tn,user_id=userid)
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

        userid= request.session['uid']
        tripno = tripd.tripnumber
        tolld = tollcharge.objects.filter(tripno = tripno , user_id=userid)
        parkd = parkingcharges.objects.filter(tripno = tripno,user_id=userid)
        guidedata = guidemod.objects.filter(tripno=tripno , user_id=userid)
        otherdata = othercharges.objects.filter(tripno = tripno , user_id=userid)
        id_list = []
        park_list = []
        guide_list =[]
        other_list =[]


        if tolld:
            for toll in tolld:
             id_list.append(toll.id)
            for x in id_list:
                echarge = request.POST.get("toll_"+str(x))
                print(echarge)
                if echarge:
                    gett = tolld.get(id=x)
                    gett.toll = echarge
                    gett.save()

            for park in parkd:
                park_list.append(park.id)
            for x in park_list:
                pcharge = request.POST.get("parking_charge_"+str(x))
                print(pcharge)
                if pcharge:
                    getp = parkd.get(id=x)
                    getp.park = pcharge
                    getp.save()

        for guide in guidedata:
            guide_list.append(guide.id)
        for x in guide_list:
            guidedata = guidemod.objects.filter(tripno=tripno)
            gcharge = request.POST.get("guide_"+str(x))
            gplace = request.POST.get("place_"+str(x))
            if gcharge:
                getg = guidedata.get(id=x)
                getg.guidecharge = gcharge
                getg.place = gplace
                getg.save()

        for other in otherdata:
            other_list.append(other.id)
        for x in other_list:
            ocharge = request.POST.get("other_"+str(x))
            if ocharge:
                geto = otherdata.get(id=x)
                geto.ocharge = ocharge
                geto.save()
        
        return redirect("tripage")

    
def delete(request,id):
    userid= request.session['uid']
    gbutton = guidemod.objects.get(id=id)
    tripno = gbutton.tripno
    tripd = tripdata.objects.get(tripnumber=tripno, user_id =userid)
    tid = tripd.id
    gbutton.delete()
    gbutton.save()
    return redirect('edit',tid)

def pdelete(request,id):
    userid= request.session['uid']
    pbutton = parkingcharges.objects.get(id=id)
    tripno = pbutton.tripno
    tripd = tripdata.objects.get(tripnumber=tripno, user_id =userid)
    pid = tripd.id
    pbutton.delete()
    return redirect('edit',pid)

def tdelete(request,id):
    userid= request.session['uid']
    tbutton = tollcharge.objects.get(id=id)
    tripno = tbutton.tripno
    tripd = tripdata.objects.get(tripnumber=tripno, user_id =userid)
    tid = tripd.id
    tbutton.delete()
    return redirect('edit',tid)

def odelete(request,id):
    userid= request.session['uid']
    obutton = othercharges.objects.get(id=id)
    tripno = obutton.tripno
    tripd = tripdata.objects.get(tripnumber=tripno, user_id =userid)
    tid = tripd.id
    obutton.delete()
    return redirect('edit',tid)
    
def remarks(request):
    review = contact.objects.all()
    return render(request , "review.html" ,{'review':review})
