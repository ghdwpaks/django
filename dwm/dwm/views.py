
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
        
        UserObj = User.objects.get(username=username)
        UserObj = authenticate(username=username, password=userpassword,nickname=UserObj.nickname,userid=UserObj.id)
        if UserObj:
            login(req, UserObj)
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
        UserObj = User.objects.get(id=tid)
        
        usernickname = req.POST.get("nickname")                                  
        print("dwm views mod usernickname :",usernickname)
        print("dwm views mod type(usernickname) :",usernickname)

        usercomment = req.POST.get("ucomm")
        print("dwm views mod usercomment :",usercomment)
        print("dwm views mod type(usercomment) :",usercomment)

        useremail = req.POST.get("umail")
        print("dwm views mod useremail :",useremail)
        print("dwm views mod type(useremail) :",useremail)

        userpicture = req.FILES.get("upic")
        print("dwm views mod userpicture :",userpicture)
        print("dwm views mod type(userpicture) :",userpicture)

        UserObj.nickname = usernickname
        UserObj.comment = usercomment
        UserObj.email = useremail

        if not userpicture == None :
            UserObj.photo = userpicture
        UserObj.save()
        

        return redirect("dwm:index")
    return render(req, "dwm/mod.html")


