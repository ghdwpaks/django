
from re import L
from django.db import models
from datetime import datetime
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from dwm.models import User
# Create your models here.


class Reply(models.Model) :
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    comment_id = models.IntegerField(default=0)
    reply_writerops = models.ForeignKey(User, related_name="reply", on_delete=models.CASCADE, db_column="reply_writerops")
    reply_comment = models.TextField(help_text="Reply Comment", blank=False, null=False)
    credate = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return str(self.id)+":"+str(self.comment_id)+":"+str(self.reply_writerops.username)+":"+str(self.reply_comment)
        
class Board(models.Model) :
    
    
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    writerops =  models.ForeignKey(User, related_name="board", on_delete=models.CASCADE, db_column="writerops")
    credate = models.DateTimeField(default=datetime.now())
    name = models.CharField(max_length=100,default="게시글",blank=True)
    thumbnail = models.ImageField(upload_to=("low/boardpic/"),blank=True,default=None)
    boardfile = models.FileField(upload_to=("boardpic/"),blank=True,default=None)
    comment = models.TextField(blank=True)
    hits = models.IntegerField(default=0)
    
    
    def getthum(self):
        print("board models Board getthum")
        if self.thumbnail:
            print("self.thumbnail.url :",self.thumbnail.url)
            print("str(self.thumbnail.url).split('.')[-1] :",str(self.thumbnail.url).split(".")[-1])
            print("str(self.thumbnail.url).split('.')[-1] in ['png','jpg','jpeg'] :",str(self.thumbnail.url).split('.')[-1] in ['png','jpg','jpeg'])
            if not str(self.thumbnail.url).split('.')[-1] in ['png','jpg','jpeg'] :
               return "/media/nnopho.png"
            return self.thumbnail.url
        return "/media/nno.jpg"


    def getfilename(self):
        print("board models Board getfilename")
        print("board models Board getfilename self.boardfile :",self.boardfile)
        if self.boardfile:
            res = self.boardfile
            if type(res) == type("") :
               res = res.split("/")[-1] 
               print("board models Board getfilename if if res :",res)
            return res
        return None

    def getid(self) :
        return self.id

        
    

    def __str__(self):
        return str(self.id)+" "+str(self.name)