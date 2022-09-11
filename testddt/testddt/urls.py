from django.urls import path

from . import views
app_name = "testddt"
urlpatterns = [
    path('index/',views.index,name="index"),
    path('',views.gotoindex,name="top"),
]