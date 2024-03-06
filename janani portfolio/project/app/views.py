from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Datas

def index(request):
   template=loader.get_template('index.html')
   return HttpResponse(template.render())
    
    
def homi(request):
    template=loader.get_template('homi.html')
    return HttpResponse(template.render())

def about(request):
    template=loader.get_template('about.html')
    return HttpResponse(template.render())

def skill(request):
    template=loader.get_template('skill.html')
    return HttpResponse(template.render())

def contact(request):
    mydata=Datas.objects.all()
    if(mydata!=""):
        return render(request,"contact.html",{"datas":mydata})
    else:
        return render(request,"contact.html")    





    
def addData(request):
    if request.method=="POST":
        name=request.POST["Fullname"]
        email=request.POST["Email"]
        message=request.POST["Message"]

        obj=Datas()
        obj.Fullname=name
        obj.Email=email
        obj.Message=message
        obj.save()
        mydata=Datas.objects.all()
        return redirect("contact")
    return render(request,"contact.html")

       
        
        
        
    
       




# Create your views here.
