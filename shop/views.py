from django.shortcuts import render,redirect
from .models import Shop

# Create your views here.

def gotoindex(req) :
    return redirect("shop:index")
def index(req) :
    s = Shop.objects.all()
    context = {
        "s" : s
    }

    return render(req,"shop/index.html",context)