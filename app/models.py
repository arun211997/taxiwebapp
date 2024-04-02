from django.db import models
from django.contrib.auth import get_user_model
user= get_user_model ()

# Create your models here.
class userdata(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    phone=models.TextField(max_length=255)

class trip(models.Model):
    tripnumber=models.TextField(default='TRIP000')

class tripdata(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    tripnumber=models.TextField(null=True)
    drivername=models.TextField(null=True)
    guestname=models.TextField(null=True)
    fromdate=models.DateField(null=True)
    todate=models.DateField(null=True)
    start=models.TextField(null=True)
    end=models.TextField(null=True)
    startkm=models.TextField(null=True)
    endkm=models.TextField(null=True)
    vehiclename=models.TextField(null=True)
    vehiclenumber=models.TextField(null=True)
    parking=models.TextField(null=True)
    toll=models.TextField(null=True)
    tripkm=models.TextField(null=True)
    total=models.TextField(null=True)
    advance=models.TextField(null=True)
    balance=models.TextField(null=True)
    fixed=models.TextField(null=True)
    extra=models.TextField(null=True)