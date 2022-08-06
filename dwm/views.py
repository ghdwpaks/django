
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.

def gotoindex(req) :
    return redirect("dwm:index")

def index(req) :
    print("type(req) :",type(req))
    return render(req,"dwm/index.html")


def join(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        uc = request.POST.get("ucomm")
        ue = request.POST.get("umail")
        uni = request.POST.get("unick")
        pi = request.FILES.get("upic")
        User.objects.create_user(username=un, password=up, nickname=uni,comment=uc, email=ue, photo=pi)
        return redirect("dwm:index")
    return render(request, "dwm/join.html")

def userlogin(req):
    if req.method == "POST":
        un = req.POST.get("uname")
        up = req.POST.get("upass")
        
        u = User.objects.get(username=un)
        u = authenticate(username=un, password=up,nickname=u.nickname,userid=u.id)
        if u:
            login(req, u)
            return redirect("dwm:index")
        else:
            pass 
    return render(req, "dwm/login.html")


def userlogout(req):
    logout(req)
    return redirect("dwm:index")

def mod(req) : 
    #req : request
    #tid : target id
    if req.method == "POST":
        print("dwm views mod req.session :",req.session)
        tid = req.user.id
        print("dwm views mod tid :",tid)
        u = User.objects.get(id=tid)
        
        uni = req.POST.get("nickname")                                  
        print("dwm views mod uni :",uni)
        print("dwm views mod type(uni) :",uni)

        uc = req.POST.get("ucomm")
        print("dwm views mod uc :",uc)
        print("dwm views mod type(uc) :",uc)

        ue = req.POST.get("umail")
        print("dwm views mod ue :",ue)
        print("dwm views mod type(ue) :",ue)

        pi = req.FILES.get("upic")
        print("dwm views mod pi :",pi)
        print("dwm views mod type(pi) :",pi)

        u.nickname = uni
        u.comment = uc
        u.email = ue

        if not pi == None :
            u.photo = pi
        u.save()
        

        return redirect("dwm:index")
    return render(req, "dwm/mod.html")


