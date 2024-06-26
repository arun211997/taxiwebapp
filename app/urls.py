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
     path('tripage',views.tripage,name='tripage'),
     path('startrip',views.startrip,name='startrip'),
     path('bill/<int:id>',views.bill,name='bill'),
     path('taxiland',views.taxiland,name='taxiland'),
     path('edit/<int:id>',views.edit,name='edit'),
     path('apply/<int:id>',views.apply,name='apply'),
     path('review',views.review,name='review'),
     path('remarks',views.remarks,name='remarks'),
     path('delete/<int:id>',views.delete,name='delete'),
     path('pdelete/<int:id>',views.pdelete,name='pdelete'),
     path('tdelete/<int:id>',views.tdelete,name='tdelete'),
     path('odelete/<int:id>',views.odelete,name='odelete'),
]    
