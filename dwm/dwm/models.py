
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.
class User(AbstractUser) :
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nickname = models.CharField(max_length=50,default="사용자",blank=True)
    email = models.CharField(max_length=50,default="def@def",blank=True)
    photo = models.ImageField(upload_to=("usrprophoto/"),blank=True)
    comment = models.TextField(blank=True)
    credate = models.DateTimeField(default=datetime.now())
    deldate = models.DateTimeField(null=True)
    repcount = models.IntegerField(default=0)
    
    def getphoto(self):
        # print("dwm models User getphoto")
        if self.photo:
            # print("self.photo.url :",self.photo.url)
            return self.photo.url
        return "/media/no.jpg"



class Subscribe(models.Model) :
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    mainuser = models.ForeignKey(User, related_name="mainuser",on_delete=models.CASCADE,null=True)
    subscriber = models.ForeignKey(User, related_name="subscriber",on_delete=models.DO_NOTHING,null=True)
    
    

    def __str__(self):
        return str(self.mainuser)+" / "+str(self.subscriber)
