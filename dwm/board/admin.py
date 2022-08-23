from django.contrib import admin
from .models import Board,Reply,File,Likey
# Register your models here.
    
admin.site.register(Board)
admin.site.register(Reply)
admin.site.register(File)
admin.site.register(Likey)