from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Shop(models.Model) :
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100,default="상품",blank=True)
    number = models.IntegerField(default=0)

    

# Create your models here.
class User(AbstractUser) :
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nickname = models.CharField(max_length=50,default="사용자",blank=True)
    comment = models.TextField(blank=True)
    repcount = models.IntegerField(default=0)
    
    def getphoto(self):
        # print("dwm models User getphoto")
        if self.photo:
            # print("self.photo.url :",self.photo.url)
            return self.photo.url
        return "/media/no.jpg"

