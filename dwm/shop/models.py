from django.db import models

# Create your models here.

class Shop(models.Model) :
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100,default="상품",blank=True)
    pic = models.ImageField(upload_to=("shoppic/"),blank=True)
    comment = models.TextField(blank=True)
    price = models.IntegerField(default=0)

    
    def getpic(self):
        # print("shop models Shop getpic")
        if self.pic:
            # print("self.pic.url :",self.pic.url)
            return self.pic.url
        return "/media/nno.jpg"
        
    def __str__(self):
        return str(self.id)+" "+str(self.name)