from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from .models import Board

# Create your views here.

    
def index(request):
    pg = request.GET.get("page",1)
    cate = request.GET.get("cate" ,"")
    kw = request.GET.get("kw","")
    order = request.GET.get("o","di")
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
            b = Board.objects.filter(content__contains=kw)
    else:
        b = Board.objects.all()
    if order == "ud":
        b = Board.objects.order_by('credate')
    elif order == "dd" :
        b = Board.objects.order_by('-credate')
    if order == "ui":
        b = Board.objects.order_by('id')
    elif order == "di" :
        b = Board.objects.order_by('-id')
    pag = Paginator(b, 5)
    obj = pag.get_page(pg)
    context = {
        "b" : obj,
        "cate" : cate,
        "kw" : kw
    }
    return render(request, "board/index.html", context)
