from django.db import models
from datetime import datetime
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
            return self.thumbnail.url
        return "/media/no.jpg"
        
    def __str__(self):
        return str(self.id)+" "+str(self.name)
