
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
        username = request.POST.get("uname")
        userpassword = request.POST.get("upass")
        usercomment = request.POST.get("ucomm")
        useremail = request.POST.get("umail")
        usernickname = request.POST.get("unick")
        userpicture = request.FILES.get("upic")
        User.objects.create_user(username=username, password=userpassword, nickname=usernickname,comment=usercomment, email=useremail, photo=userpicture)
        return redirect("dwm:index")
    return render(request, "dwm/join.html")

def userlogin(req):
    if req.method == "POST":
        username = req.POST.get("uname")
        userpassword = req.POST.get("upass")
        
        userobj = User.objects.get(username=username)
        userobj = authenticate(username=username, password=userpassword,nickname=userobj.nickname,userid=userobj.id)
        if userobj:
            login(req, userobj)
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
        tid = req.user.id
        userobj = User.objects.get(id=tid)
        # print("dwm views mod req.session :",req.session)
        # print("dwm views mod tid :",tid)
        
        usernickname = req.POST.get("nickname")                                  
        usercomment = req.POST.get("ucomm")
        useremail = req.POST.get("umail")
        userpicture = req.FILES.get("upic")
        # print("dwm views mod usernickname :",usernickname)
        # print("dwm views mod type(usernickname) :",usernickname)
        # print("dwm views mod usercomment :",usercomment)
        # print("dwm views mod type(usercomment) :",usercomment)
        # print("dwm views mod useremail :",useremail)
        # print("dwm views mod type(useremail) :",useremail)
        # print("dwm views mod userpicture :",userpicture)
        # print("dwm views mod type(userpicture) :",userpicture)

        userobj.nickname = usernickname
        userobj.comment = usercomment
        userobj.email = useremail

        if not userpicture == None :
            userobj.photo = userpicture
        userobj.save()
        

        return redirect("dwm:index")
    return render(req, "dwm/mod.html")


