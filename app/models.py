from django.db import models
from django.contrib.auth import get_user_model
user= get_user_model ()

# Create your models here.
class userdata(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    phone=models.TextField(max_length=255)

class trip(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    tripnumber=models.TextField(default="TRIP000")

class tripdata(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    tripnumber=models.TextField(null=True)
    drivername=models.TextField(null=True)
    guestname=models.TextField(null=True)
    fromdate=models.TextField(null=True)
    todate=models.TextField(null=True)
    start=models.TextField(null=True)
    end=models.TextField(default=0)
    startkm=models.TextField(null=True)
    endkm=models.TextField(default=0)
    vehiclename=models.TextField(null=True)
    vehiclenumber=models.TextField(null=True)
    parking=models.TextField(default=0)
    toll=models.TextField(default=0)
    tripkm=models.TextField(default=0)
    total=models.TextField(default=0)
    advance=models.TextField(default=0)
    balance=models.TextField(default=0)
    tripcharge=models.TextField(null=True)
    guidecharge=models.TextField(null=True)
    huncharge=models.TextField(null=True)
    extra=models.TextField(null=True)
    other=models.TextField(null=True)

class contact(models.Model):
    name = models.TextField()
    phone = models.TextField()
    review = models.TextField()

class guidemod(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    tripno = models.TextField(null=True)
    guidecharge = models.TextField(null=True)
    place = models.TextField(null=True)

class tollcharge(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    tripno = models.TextField(null=True)
    toll = models.TextField(null=True)

class parkingcharges(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    tripno = models.TextField()
    park = models.TextField()

class othercharges(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    tripno = models.TextField(null=True)
    ocharge = models.TextField(default=0)

