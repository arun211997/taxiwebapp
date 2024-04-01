from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('',views.login,name='login'),
     path('signup',views.signup,name='signup'),
     path('mainpage',views.mainpage,name='mainpage'),
     path('signupfunct',views.signupfunct,name='signupfunct'),
     path('log',views.log,name='log'),
     path('logout',views.logout,name='logout'),
]