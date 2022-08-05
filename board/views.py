from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from .models import Board
from django.utils import timezone
from dwm.models import User
# Create your views here.

    
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
        un = req.user.username
        uni = req.user.nickname
        thum = req.FILES.get("thum")
        n = req.POST.get("name")
        c = req.POST.get("com")
        print("board views create")
        print("un :",un)
        print("uni :",uni)
        print("thum :",thum)
        print("n :",n)
        print("c :",c)
        Board(name=n, comment=c, writername=un,thumbnail=thum,writernick=uni,credate=timezone.now()).save()
        return redirect("board:index")

    return render(req, "board/create.html")