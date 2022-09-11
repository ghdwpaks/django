from django.shortcuts import render,redirect
from .models import Shop


def index(req) :
    shopobj = Shop.objects.all()
    print("shopobj :",shopobj)
    print("len(shopobj) :",len(shopobj))
    context = {
        "s" : shopobj
    }

    return render(req,"index.html",context)
    
def gotoindex(req) :
    return redirect("testddt:index")