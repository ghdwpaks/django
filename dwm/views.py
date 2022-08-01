
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.

def index(req) :
    print("type(req) :",type(req))
    return render(req,"dwm/index.html")


def join(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        uc = request.POST.get("ucomm")
        ue = request.POST.get("umail")
        pi = request.FILES.get("upic")
        User.objects.create_user(username=un, password=up, comment=uc, email=ue, photo=pi)
        return redirect("dwm:index")
    return render(request, "dwm/join.html")

def userlogin(req):
    if req.method == "POST":
        un = req.POST.get("uname")
        up = req.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:
            login(req, u)
            return redirect("dwm:index")
        else:
            pass 
    return render(req, "dwm/login.html")


def userlogout(req):
    logout(req)
    return redirect("dwm:index")

