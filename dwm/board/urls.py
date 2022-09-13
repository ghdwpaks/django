from django.shortcuts import render
from django.urls import path , include
from . import views
# Create your views here.
app_name = "board"
urlpatterns = [
    path('index/',views.index,name="index"),
    path('create/',views.create,name="create"),
    path('down/',views.down,name="down"),
    path('detail/<tr>',views.detail,name="detail"),
    path('userdetail/<tr>',views.userdetail,name="userdetail"),
    path('sub/<userid>',views.sub,name="sub"),
    path('unsub/<userid>',views.unsub,name="unsub"),
    path('mod/<tr>',views.mod,name="mod"),
    path('likey/<likeytarget>',views.likey,name="likey"),
    path('unlikey/<unlikeytarget>',views.unlikey,name="unlikey"),
    path('imgdel/<imgid>/<boardtr>',views.imgdel,name="imgdel"),
    path('delete/<tr>',views.delete,name="delete"),
    path('reply/<tr>',views.reply,name="reply"),
    path('reply/del/<replytr>/<boardtr>',views.replydel,name="replydel"),
    path('createcontentautomaticly/',views.createcontentautomaticly,name="createcontentautomaticly"),
    path('__debug__/', include('debug_toolbar.urls')),
    path('',views.gotoindex,name="top"),
]

 