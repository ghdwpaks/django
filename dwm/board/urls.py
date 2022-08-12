from django.shortcuts import render
from django.urls import path
from . import views
# Create your views here.
app_name = "board"
urlpatterns = [
    path('index/',views.index,name="index"),
    path('create/',views.create,name="create"),
    path('down/',views.down,name="down"),
    path('detail/<tr>',views.detail,name="detail"),
    path('mod/<tr>',views.mod,name="mod"),
    path('delete/<tr>',views.delete,name="delete"),
    path('reply/<tr>',views.reply,name="reply"),
    path('',views.gotoindex,name="top")
]

 