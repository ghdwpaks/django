from django.shortcuts import render
from django.urls import path
from . import views
# Create your views here.
app_name = "board"
urlpatterns = [
    path('index/',views.index,name="index"),
]

