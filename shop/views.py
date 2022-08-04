from django.shortcuts import render
from .models import Shop

# Create your views here.

def index(req) :
    s = Shop.objects.all()
    context = {
        "s" : s
    }

    return render(req,"shop/index.html",context)