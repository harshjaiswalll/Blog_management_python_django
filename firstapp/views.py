#from os import uname
import email
from re import A
from turtle import title
from unittest import removeResult
from urllib import request
#from xml.dom import UserDataHandler
from django.shortcuts import render,HttpResponse, redirect
from .models import User, Createblok;
from django.contrib import messages;
from django.core.files.storage import FileSystemStorage


    # Create your views here.
def home(request):
    return render(request,"home.html")
    #return HttpResponse("<h1> WELLCOME HARSH index</h1>");

def about(request):
    #return HttpResponse("<h1> WELLCOME HARSH about</h1>");
    return render(request,"about.html")

def blogread(request):
    #return HttpResponse("<h1> WELLCOME HARSH about</h1>");
    return render(request,"blogread.html")

def contact(request):
    #return HttpResponse("<h1> WELLCOME  HARSH  serVICES</h1>");
    return render(request,"contact.html")

def showdata(request):
    userdata = User.objects.all().order_by('id').reverse();
    myrec ={ "records": userdata};
    return render(request,"showdata.html", myrec);


def delete(request):
    if request.method == "GET":
        uid = request.GET.get("sid");
        User.objects.filter(id=uid).delete();
        userdata = User.objects.all();
        myrec = { "records": userdata};
        return render(request, "showdata.html",myrec)


# def adduser(request):
#     return render(request, "signup.html");




def signup(request):
    if request.method == "POST":
        uname = request.POST.get("nm");
        ueid = request.POST.get("eid");
        upwd = request.POST.get("pwd");
        uage = request.POST.get("age");

        user = User(name = uname, email = ueid, password=upwd, age = uage);
        user.save();
        messages.success(request, 'User Sucessfully submitted');
    return render(request, "signup.html");

def login(request):
    if request.method == "POST":
        ueid = request.POST.get("eid");
        upwd = request.POST.get("pwd");
        data = User.objects.filter(email = ueid, password = upwd).exists();
        if(data):
            return redirect("/dashboard/");
           # return render(request, "dashboard.html")
        else:
            return render(request, "login.html")
    return render(request, "login.html")

def edit (request):
    editid=request.GET.get("editid");
    editdata = User.objects.filter(id=editid).all();
    return render(request ,"edit.html",{"userdata" : editdata});

def update(request):
    if request.method == "POST":
        id = request.POST.get("id");
        uname = request.POST.get("nm");
        ueid = request.POST.get("eid");
        upwd = request.POST.get("pwd");
        uage = request.POST.get("age");
        User.objects.filter(id=id).update(name=uname ,email=ueid ,password=upwd, age=uage);
        userdata = User.objects.all();
        myrec = { "records": userdata};
        return render(request, "showdata.html",myrec);


def dashboard(request):
    return render(request, "dashboard.html")

# it is use for photo
def createblok(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        btitle = request.POST.get("tl");
        bemail = request.POST.get("eml");
        bphoto = request.POST.get("img");
        byoublok = request.POST.get("yb");
        #
        user = Createblok(title = btitle, email = bemail,photo=filename, youblok=byoublok)
        user.save()
    return render(request, "createblok.html");


def blogshow(request):
    blogdata = Createblok.objects.all();
    mydata = {"record":blogdata};
    return render(request,"blogread.html",mydata)
    
