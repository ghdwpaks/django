from django.urls import path

from . import views
app_name = "shop"
urlpatterns = [
    path('index/',views.index,name="index")
]