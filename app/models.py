from django.db import models
from django.contrib.auth import get_user_model
user= get_user_model ()

# Create your models here.
class userdata(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    phone=models.TextField(max_length=255)