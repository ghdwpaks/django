from django.urls import path

from . import views
app_name = "dwm"
urlpatterns = [
    path('index/',views.index,name="index"),
    path('join/',views.join,name="join"),
    path('login/',views.userlogin,name="login"),
    path('logout/',views.userlogout,name="logout"),
    path('mod/',views.mod,name="mod")
]