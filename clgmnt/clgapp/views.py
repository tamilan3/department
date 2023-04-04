from django.shortcuts import render
import datetime
def index(request):
    return render (request,'clgapp/index.html')

def login(request):
    return render(request,"clgapp/login.html")

def sighnup(request):
    return render(request,"clgapp/register.html")

def home(request):
    crtime=datetime.datetime.now()
    crtime.hour
    if crtime.hour <12:
        greet="Good Morning"
    elif crtime.hour <18:
        greet="Good Afternoon"
    else:
        greet="Good Night"

    context={
            'greet':greet,
        }    
    return render(request,"clgapp/home.html",context) 


# Create your views here.
