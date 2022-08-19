
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
    comment = models.TextField(blank=True)
    hits = models.IntegerField(default=0)
    public = models.BooleanField(blank=True, default=True)
    
    
    def getthum(self):
        # print("board models Board getthum")
        if self.thumbnail:
            # print("board models Board getthum self.thumbnail.url :",self.thumbnail.url)
            # print("board models Board getthum str(self.thumbnail.url).split('.')[-1] :",str(self.thumbnail.url).split(".")[-1])
            # print("board models Board getthum str(self.thumbnail.url).split('.')[-1] in ['png','jpg','jpeg'] :",str(self.thumbnail.url).split('.')[-1] in ['png','jpg','jpeg'])
            # print("board models Board getthum not str(self.thumbnail.url).split('.')[-1] in ['png','jpg','jpeg'] :",not str(self.thumbnail.url).split('.')[-1] in ['png','jpg','jpeg'])
            if not str(self.thumbnail.url).split('.')[-1] in ['png','jpg','jpeg'] :
               return "/media/nnopho.png"
            return self.thumbnail.url
        return "/media/nnopho.jpg"
        
    

    def __str__(self):
        return str(self.id)+" "+str(self.name)

class File(models.Model) :
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    boardops = models.ForeignKey(Board, related_name="file",on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to=('boardpic/'),blank=True, null=True)
    def __str__(self):
        return str(self.boardops.name)+" "+str(self.id)