
from re import L
from django.db import models
from datetime import datetime
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
# Create your models here.

class Board(models.Model) :
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    writername = models.CharField(max_length=100)
    writernick = models.CharField(max_length=100,default=None)
    credate = models.DateTimeField(default=datetime.now())
    name = models.CharField(max_length=100,default="게시글",blank=True)
    thumbnail = models.ImageField(upload_to=("boardpic/"),blank=True)
    comment = models.TextField(blank=True)
    hits = models.IntegerField(default=0)
    
    
    def getthum(self):
        print("board models Board getthum")
        if self.thumbnail:
            print("self.thumbnail.url :",self.thumbnail.url)
            print("str(self.thumbnail.url).split('.')[-1] :",str(self.thumbnail.url).split(".")[-1])
            print("str(self.thumbnail.url).split('.')[-1] in ['png','jpg','jpeg'] :",str(self.thumbnail.url).split('.')[-1] in ['png','jpg','jpeg'])
            if not str(self.thumbnail.url).split('.')[-1] in ['png','jpg','jpeg'] :
               return "/media/nopho.png"
            return self.thumbnail.url
        return "/media/no.jpg"


    def getfilename(self):
        print("board models Board getfilename")
        print("board models Board getfilename self.thumbnail :",self.thumbnail)
        if self.thumbnail:
            res = self.thumbnail.url
            if type(res) == type("") :
               res = res.split("/")[-1] 
               print("board models Board getfilename if if res :",res)
            return res
        return None
        
        
    

    def __str__(self):

        return str(self.id)+" "+str(self.name)
