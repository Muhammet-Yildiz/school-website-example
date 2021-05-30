from django.shortcuts import render,redirect,get_object_or_404

from .models import *
# Create your views here.
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
# ajax posttan gelen bilgileri almak için ve cookies lerden bılgı almak için kullanıyoruz json ' ı 
import json 
from datetime import datetime

from django.contrib.auth import login,authenticate,logout

def home (request) :

    news = News.objects.all()
    announcements = Announcements.objects.all()
    banners = Banner.objects.all()
    studentsNews = Students.objects.all()
    advertisements = Advertisementss.objects.all()
    automatıons = Automatıons.objects.all()
    context = {
        'news':news,
        'announcements':announcements,
        'banners':banners,
        'studentsNews': studentsNews,
        'advertisements':advertisements,
        'automatıons':automatıons
    }

    return render(request ,"index.html" ,context)

def newsDetail(request,slug_text) : 
    targetnews = News.objects.filter(slug =slug_text )
    
    for target in targetnews : 
        targetId =target.id 

        target.see += 1 

        target.save()

    all_news = News.objects.all()
    context = {
        'targetnews':targetnews ,
        'all_news':all_news,
        'targetId':targetId

    }

    return render(request ,"newsDetail.html" ,context)

def announcementDetail(request,slug_text) :
    targetannouncement= Announcements.objects.filter(slug =slug_text )
    
    for target in targetannouncement : 
        targetId =target.id 

        target.see += 1 

        target.save()

    all_announcement = Announcements.objects.all()
    context = {
        'targetannouncement':targetannouncement ,
        'all_announcement':all_announcement,
        'targetId':targetId

    }
    return render(request ,"announcementDetail.html" ,context)


def studentNewsDetail(request,slug_text) :
    targetstudentNews= Students.objects.filter(slug =slug_text )
    
    for target in targetstudentNews : 
        targetId =target.id 

        target.see += 1 

        target.save()

    all_studentNews = Students.objects.all()
    context = {
        'targetstudentNews':targetstudentNews ,
        'all_studentNews':all_studentNews,
        'targetId':targetId

    }
    return render(request ,"studentNewsDetail.html" ,context)



def advertisementsDetail(request,slug_text) :
    targetadvertisement= Advertisementss.objects.filter(slug =slug_text )
    
    for target in targetadvertisement : 
        targetId =target.id 

        target.see += 1 

        target.save()

    all_advertisement = Advertisementss.objects.all()
    context = {
        'targetadvertisement':targetadvertisement ,
        'all_advertisement':all_advertisement,
        'targetId':targetId

    }
    return render(request ,"advertisementsDetail.html" ,context)





def loginuser(request):
  
    if request.method == "POST" :

     
        data = json.loads(request.body)
        domain_name = data['domain_Name']
        password = data['passwordValue']
        username = data['usernameValue']

  
        print("username",username)
        print("parola",password)
        print("domain adı ",domain_name)
        
        searchEmail = username+"@"+domain_name

        print("ARANACAK EMAİL ",searchEmail)

        if (User.objects.filter(email = searchEmail).exists()):
            username = User.objects.get(email = searchEmail).username
        else :
            username = None

        user =authenticate(username =username,password =password)

        if user is  None :
            return  JsonResponse({'bool':False,'Error_Message':'Kullanıcı Adı  yada Parola  hatalı'},safe =False )
            
        else :
            login(request, user)
            return  JsonResponse({'bool':True,'Success_Message':'Başarıyla giriş yaptınız'},safe =False )
 
    else :
        # demekki get request 
        return render(request,"user/login.html")





def logoutUser(request):    
    logout(request) 
    messages.success(request,"Başarıyla Çıkış yaptınız ")
    return redirect("home")
