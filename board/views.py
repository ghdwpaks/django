from audioop import reverse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Board
from django.utils import timezone
from django.http import HttpResponseRedirect
from dwm.models import User
# Create your views here.

def gotoindex(req) :
    return redirect("board:index")
    
def index(req):
    global User
    pg = req.GET.get("page",1)
    cate = req.GET.get("cate" ,"")
    kw = req.GET.get("kw","")
    order = req.GET.get("o","di")
    #d : date
    #ud : upper date
    #dd : downer date
    #i : id
    #ui : upper id
    #di : downer id

    if kw:
        if cate == "sub":
            b = Board.objects.filter(subject__startswith=kw)
        elif cate == "wri":
            try:
                from dwm.models import User
                u = User.objects.get(username=kw)
                b = Board.objects.filter(writername=u)
            except:
                b = Board.objects.none()
        elif cate == "con":
            b = Board.objects.filter(comment__contains=kw)
    else:
        b = Board.objects.all()
    if order == "ud":
        b = b.order_by('credate')
    elif order == "dd" :
        b = b.order_by('-credate')
    if order == "ui":
        b = b.order_by('id')
    elif order == "di" :
        b = b.order_by('-id')
    writers = b.values('writername')
    writers = writers.distinct()
    #print("board views index writers :",writers)
    #print("board views index type(writers) :",type(writers))
    diswriters = []
    for i in writers : 
        #print("i : ",i)
        #print("type(i) : ",type(i))
        diswriters.append(i['writername'])
    diswriters = set(diswriters)
    diswriters = list(diswriters)
    #print("board views index diswriters :",diswriters)
    #print("board views index writers.values() :",writers.values())
    phs = []
    for i in range(len(diswriters)) :
        #print("board views index for i diswriters[i] :",diswriters[i])
        tempphs = User.objects.get(username=diswriters[i])
        #print("board views index for i tempphs 1 :",tempphs)
        #print("board views index for i type(tempphs) 1 :",type(tempphs))
        tempphs = User.getphoto(tempphs)
        #print("board views index for i tempphs 2 :",tempphs)
        #print("board views index for i type(tempphs) 2 :",type(tempphs))
        #print("board views index for i {diswriters[i]:tempphs} :",{diswriters[i]:tempphs})
        
        phs.append({diswriters[i]:tempphs})
    print("board views index phs :",phs)
    #print("board views index type(phs) :",type(phs))

    pag = Paginator(b, 5)
    obj = pag.get_page(pg)
    context = {
        "b" : obj,
        "cate" : cate,
        "kw" : kw,
        "phs" : phs
    }
    return render(req, "board/index.html", context)

def create(req):
    if req.method == "POST":
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            un = req.user.username
            uni = req.user.nickname
            thum = req.FILES.get("thum")
            n = req.POST.get("name")
            c = req.POST.get("com")
            print("board views create post")
            print("un :",un)
            print("uni :",uni)
            print("thum :",thum)
            print("n :",n)
            print("c :",c)
            Board(name=n, comment=c, writername=un,thumbnail=thum,writernick=uni,credate=timezone.now()).save()
            return redirect("board:index")
    
    elif req.method == "GET":
        print("board views create get")
        print("board views create get req.user.username :",req.user.username)
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            return render(req, "board/create.html")


def mod(req, tr):
    if req.method == "POST":
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            r = Board.objects.get(id=tr)
            print("board views mod r.writername :",r.writername)
            print("board views mod req.user.username :",req.user.username)
            if r.writername == req.user.username :

                rn = req.POST.get("rn")
                rt = req.FILES.get("rt")
                rc = req.POST.get("rc")
                print("board views mod if if rn :",rn)
                print("board views mod if if rt :",rt)
                print("board views mod if if rc :",rc)
                if not rt == None :
                    r.thumbnail = rt
                    print("board views mod if if if changethumnail? : yes")
                r.name = rn
                r.comment = rc
                r.save()
                b = Board.objects.get(id=tr)
                context = {
                    "b" : b
                }
                return render(req, "board/detail.html",context)
    
    elif req.method == "GET":
        print("board views create get")
        print("board views create get req.user.username :",req.user.username)
        
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            r = Board.objects.get(id=tr)
            print("board views mod r.writername :",r.writername)
            print("board views mod req.user.username :",req.user.username)
            if r.writername == req.user.username :
                print("board views mod over if")
                context = {
                    "r" : r
                }
                return render(req, "board/mod.html",context)

def detail(req, tr) :
    print("board views detail tr :",tr)
    #tr : target raw
    b = Board.objects.get(id=tr)
    #print("board views detail b :",b)
    #print("board views detail type(b) :",type(b))
    #print("board views detail b.id :",b.id)
    #print("board views detail b.writernick :",b.writernick)
    #print("board views detail b.credate :",b.credate)
    #print("board views detail b.name :",b.name)
    #print("board views detail b.thumbnail :",b.thumbnail)
    #print("board views detail b.comment :",b.comment)
    b.hits = b.hits+1
    b.save()
    
    context = {
        "b" : b
    }
    return render(req, "board/detail.html",context)