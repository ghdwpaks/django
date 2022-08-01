from django.shortcuts import render

# Create your views here.

def index(req) :
    print("type(req) :",type(req))
    return render(req,"dwm/index.html")


