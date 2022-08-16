
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
               return "/media/nnopho.png"
            return self.thumbnail.url
        return "/media/nno.jpg"


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

    def getid(self) :
        return self.id

        
    '''
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.category :",c.category)
        print("board models Board getthum if type(c.category) :",type(c.category))
    except :
        print("error from category")

    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.close :",c.close)
        print("board models Board getthum if type(c.close) :",type(c.close))
    except :
        print("error from close")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.convert :",c.convert)
        print("board models Board getthum if type(c.convert) :",type(c.convert))
    except :
        print("error from convert")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.copy :",c.copy)
        print("board models Board getthum if type(c.copy) :",type(c.copy))
    except :
        print("error from copy")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.crop :",c.crop)
        print("board models Board getthum if type(c.crop) :",type(c.crop))
    except :
        print("error from crop")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.draft :",c.draft)
        print("board models Board getthum if type(c.draft) :",type(c.draft))
    except :
        print("error from draft")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.effect_spread :",c.effect_spread)
        print("board models Board getthum if type(c.effect_spread) :",type(c.effect_spread))
    except :
        print("error from effect_spread")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.encoderconfig :",c.encoderconfig)
        print("board models Board getthum if type(c.encoderconfig) :",type(c.encoderconfig))
    except :
        print("error from encoderconfig")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.encoderinfo :",c.encoderinfo)
        print("board models Board getthum if type(c.encoderinfo) :",type(c.encoderinfo))
    except :
        print("error from encoderinfo")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.entropy :",c.entropy)
        print("board models Board getthum if type(c.entropy) :",type(c.entropy))
    except :
        print("error from entropy")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.filter :",c.filter)
        print("board models Board getthum if type(c.filter) :",type(c.filter))
    except :
        print("error from filter")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.format_description :",c.format_description)
        print("board models Board getthum if type(c.format_description) :",type(c.format_description))
    except :
        print("error from format_description")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.frombytes :",c.frombytes)
        print("board models Board getthum if type(c.frombytes) :",type(c.frombytes))
    except :
        print("error from frombytes")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.getbands :",c.getbands)
        print("board models Board getthum if type(c.getbands) :",type(c.getbands))
    except :
        print("error from getbands")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.getbbox :",c.getbbox)
        print("board models Board getthum if type(c.getbbox) :",type(c.getbbox))
    except :
        print("error from getbbox")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.getchannel :",c.getchannel)
        print("board models Board getthum if type(c.getchannel) :",type(c.getchannel))
    except :
        print("error from getchannel")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.getcolors :",c.getcolors)
        print("board models Board getthum if type(c.getcolors) :",type(c.getcolors))
    except :
        print("error from getcolors")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.getdata :",c.getdata)
        print("board models Board getthum if type(c.getdata) :",type(c.getdata))
    except :
        print("error from getdata")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.getexif :",c.getexif)
        print("board models Board getthum if type(c.getexif) :",type(c.getexif))
    except :
        print("error from getexif")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.getbbox :",c.getbbox)
        print("board models Board getthum if type(c.getbbox) :",type(c.getbbox))
    except :
        print("error from getbbox")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.getchannel :",c.getchannel)
        print("board models Board getthum if type(c.getchannel) :",type(c.getchannel))
    except :
        print("error from getchannel")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.getcolors :",c.getcolors)
        print("board models Board getthum if type(c.getcolors) :",type(c.getcolors))
    except :
        print("error from getcolors")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.getdata :",c.getdata)
        print("board models Board getthum if type(c.getdata) :",type(c.getdata))
    except :
        print("error from getdata")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.getextrema :",c.getextrema)
        print("board models Board getthum if type(c.getextrema) :",type(c.getextrema))
    except :
        print("error from getextrema")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.getim :",c.getim)
        print("board models Board getthum if type(c.getim) :",type(c.getim))
    except :
        print("error from getim")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.getpalette :",c.getpalette)
        print("board models Board getthum if type(c.getpalette) :",type(c.getpalette))
    except :
        print("error from getpalette")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.getpixel :",c.getpixel)
        print("board models Board getthum if type(c.getpixel) :",type(c.getpixel))
    except :
        print("error from getpixel")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.getprojection :",c.getprojection)
        print("board models Board getthum if type(c.getprojection) :",type(c.getprojection))
    except :
        print("error from getprojection")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.height :",c.height)
        print("board models Board getthum if type(c.height) :",type(c.height))
    except :
        print("error from height")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.histogram :",c.histogram)
        print("board models Board getthum if type(c.histogram) :",type(c.histogram))
    except :
        print("error from histogram")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.im :",c.im)
        print("board models Board getthum if type(c.im) :",type(c.im))
    except :
        print("error from im")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.info :",c.info)
        print("board models Board getthum if type(c.info) :",type(c.info))
    except :
        print("error from info")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.mode :",c.mode)
        print("board models Board getthum if type(c.mode) :",type(c.mode))
    except :
        print("error from mode")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.palette :",c.palette)
        print("board models Board getthum if type(c.palette) :",type(c.palette))
    except :
        print("error from palette")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.paste :",c.paste)
        print("board models Board getthum if type(c.paste) :",type(c.paste))
    except :
        print("error from paste")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.point :",c.point)
        print("board models Board getthum if type(c.point) :",type(c.point))
    except :
        print("error from point")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.putalpha :",c.putalpha)
        print("board models Board getthum if type(c.putalpha) :",type(c.putalpha))
    except :
        print("error from putalpha")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.putdata :",c.putdata)
        print("board models Board getthum if type(c.putdata) :",type(c.putdata))
    except :
        print("error from putdata")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.putpalette :",c.putpalette)
        print("board models Board getthum if type(c.putpalette) :",type(c.putpalette))
    except :
        print("error from putpalette")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.putpixel :",c.putpixel)
        print("board models Board getthum if type(c.putpixel) :",type(c.putpixel))
    except :
        print("error from putpixel")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.pyaccess :",c.pyaccess)
        print("board models Board getthum if type(c.pyaccess) :",type(c.pyaccess))
    except :
        print("error from pyaccess")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.quantize :",c.quantize)
        print("board models Board getthum if type(c.quantize) :",type(c.quantize))
    except :
        print("error from quantize")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.readonly :",c.readonly)
        print("board models Board getthum if type(c.readonly) :",type(c.readonly))
    except :
        print("error from readonly")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.reduce :",c.reduce)
        print("board models Board getthum if type(c.reduce) :",type(c.reduce))
    except :
        print("error from reduce")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.remap_palette :",c.remap_palette)
        print("board models Board getthum if type(c.remap_palette) :",type(c.remap_palette))
    except :
        print("error from remap_palette")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.resize :",c.resize)
        print("board models Board getthum if type(c.resize) :",type(c.resize))
    except :
        print("error from resize")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.rotate :",c.rotate)
        print("board models Board getthum if type(c.rotate) :",type(c.rotate))
    except :
        print("error from rotate")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.save :",c.save)
        print("board models Board getthum if type(c.save) :",type(c.save))
    except :
        print("error from save")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.seek :",c.seek)
        print("board models Board getthum if type(c.seek) :",type(c.seek))
    except :
        print("error from seek")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.show :",c.show)
        print("board models Board getthum if type(c.show) :",type(c.show))
    except :
        print("error from show")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.size :",c.size)
        print("board models Board getthum if type(c.size) :",type(c.size))
    except :
        print("error from size")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.split :",c.split)
        print("board models Board getthum if type(c.split) :",type(c.split))
    except :
        print("error from split")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.tell :",c.tell)
        print("board models Board getthum if type(c.tell) :",type(c.tell))
    except :
        print("error from tell")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.thumbnail :",c.thumbnail)
        print("board models Board getthum if type(c.thumbnail) :",type(c.thumbnail))
    except :
        print("error from thumbnail")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.tobitmap :",c.tobitmap)
        print("board models Board getthum if type(c.tobitmap) :",type(c.tobitmap))
    except :
        print("error from tobitmap")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.tobytes :",c.tobytes)
        print("board models Board getthum if type(c.tobytes) :",type(c.tobytes))
    except :
        print("error from tobytes")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.toqimage :",c.toqimage)
        print("board models Board getthum if type(c.toqimage) :",type(c.toqimage))
    except :
        print("error from toqimage")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.toqpixmap :",c.toqpixmap)
        print("board models Board getthum if type(c.toqpixmap) :",type(c.toqpixmap))
    except :
        print("error from toqpixmap")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.transform :",c.transform)
        print("board models Board getthum if type(c.transform) :",type(c.transform))
    except :
        print("error from transform")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.transpose :",c.transpose)
        print("board models Board getthum if type(c.transpose) :",type(c.transpose))
    except :
        print("error from transpose")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.verify :",c.verify)
        print("board models Board getthum if type(c.verify) :",type(c.verify))
    except :
        print("error from verify")
    try :
        c = dc(self.thumbnail)
        print("board models Board getthum if c.width :",c.width)
        print("board models Board getthum if type(c.width) :",type(c.width))
    except :
        print("error from width")
    '''
    '''
    board models Board getthum if c.info : {'srgb': 0, 'gamma': 0.45455, 'dpi': (96, 96)}
    board models Board getthum if type(c.info) : <class 'dict'>
    board models Board getthum if c.load : <bound method Image.load of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1790>>
    board models Board getthum if type(c.load) : <class 'method'>
    board models Board getthum if c.alpha_composite : <bound method Image.alpha_composite of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1790>>
    board models Board getthum if type(c.alpha_composite) : <class 'method'>
    board models Board getthum if c.category : 0
    board models Board getthum if type(c.category) : <class 'int'>
    board models Board getthum if c.close : <bound method Image.close of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1B80>>
    board models Board getthum if type(c.close) : <class 'method'>
    board models Board getthum if c.convert : <bound method Image.convert of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1B98>>
    board models Board getthum if type(c.convert) : <class 'method'>
    board models Board getthum if c.copy : <bound method Image.copy of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1BB0>>
    board models Board getthum if type(c.copy) : <class 'method'>
    board models Board getthum if c.crop : <bound method Image.crop of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1BC8>>
    board models Board getthum if type(c.crop) : <class 'method'>
    board models Board getthum if c.draft : <bound method Image.draft of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1BE0>>
    board models Board getthum if type(c.draft) : <class 'method'>
    board models Board getthum if c.effect_spread : <bound method Image.effect_spread of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1BF8>>
    board models Board getthum if type(c.effect_spread) : <class 'method'>
    error from encoderconfig
    error from encoderinfo
    board models Board getthum if c.entropy : <bound method Image.entropy of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1C40>>
    board models Board getthum if type(c.entropy) : <class 'method'>
    board models Board getthum if c.filter : <bound method Image.filter of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1C58>>
    board models Board getthum if type(c.filter) : <class 'method'>
    board models Board getthum if c.format_description : None
    board models Board getthum if type(c.format_description) : <class 'NoneType'>
    board models Board getthum if c.frombytes : <bound method Image.frombytes of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1C88>>
    board models Board getthum if type(c.frombytes) : <class 'method'>
    board models Board getthum if c.getbands : <bound method Image.getbands of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1CA0>>
    board models Board getthum if type(c.getbands) : <class 'method'>
    board models Board getthum if c.getbbox : <bound method Image.getbbox of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1CB8>>
    board models Board getthum if type(c.getbbox) : <class 'method'>
    board models Board getthum if c.getchannel : <bound method Image.getchannel of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1CD0>>
    board models Board getthum if type(c.getchannel) : <class 'method'>
    board models Board getthum if c.getcolors : <bound method Image.getcolors of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1CE8>>
    board models Board getthum if type(c.getcolors) : <class 'method'>
    board models Board getthum if c.getdata : <bound method Image.getdata of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1D00>>
    board models Board getthum if type(c.getdata) : <class 'method'>
    board models Board getthum if c.getexif : <bound method Image.getexif of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1D18>>
    board models Board getthum if type(c.getexif) : <class 'method'>
    board models Board getthum if c.getbbox : <bound method Image.getbbox of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1D30>>
    board models Board getthum if type(c.getbbox) : <class 'method'>
    board models Board getthum if c.getchannel : <bound method Image.getchannel of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1D48>>
    board models Board getthum if type(c.getchannel) : <class 'method'>
    board models Board getthum if c.getcolors : <bound method Image.getcolors of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1D60>>
    board models Board getthum if type(c.getcolors) : <class 'method'>
    board models Board getthum if c.getdata : <bound method Image.getdata of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1D78>>
    board models Board getthum if type(c.getdata) : <class 'method'>
    board models Board getthum if c.getextrema : <bound method Image.getextrema of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1D90>>
    board models Board getthum if type(c.getextrema) : <class 'method'>
    board models Board getthum if c.getim : <bound method Image.getim of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1DA8>>
    board models Board getthum if type(c.getim) : <class 'method'>
    board models Board getthum if c.getpalette : <bound method Image.getpalette of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1DC0>>
    board models Board getthum if type(c.getpalette) : <class 'method'>
    board models Board getthum if c.getpixel : <bound method Image.getpixel of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1DD8>>
    board models Board getthum if type(c.getpixel) : <class 'method'>
    board models Board getthum if c.getprojection : <bound method Image.getprojection of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1DF0>>
    board models Board getthum if type(c.getprojection) : <class 'method'>
    board models Board getthum if c.height : 193
    board models Board getthum if type(c.height) : <class 'int'>
    board models Board getthum if c.histogram : <bound method Image.histogram of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1E20>>
    board models Board getthum if type(c.histogram) : <class 'method'>
    board models Board getthum if c.im : <ImagingCore object at 0x0E246660>
    board models Board getthum if type(c.im) : <class 'ImagingCore'>
    board models Board getthum if c.info : {'srgb': 0, 'gamma': 0.45455, 'dpi': (96, 96)}
    board models Board getthum if type(c.info) : <class 'dict'>
    board models Board getthum if c.mode : RGB
    board models Board getthum if type(c.mode) : <class 'str'>
    board models Board getthum if c.palette : None
    board models Board getthum if type(c.palette) : <class 'NoneType'>
    board models Board getthum if c.paste : <bound method Image.paste of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1E98>>
    board models Board getthum if type(c.paste) : <class 'method'>
    board models Board getthum if c.point : <bound method Image.point of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1EB0>>
    board models Board getthum if type(c.point) : <class 'method'>
    board models Board getthum if c.putalpha : <bound method Image.putalpha of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1EC8>>
    board models Board getthum if type(c.putalpha) : <class 'method'>
    board models Board getthum if c.putdata : <bound method Image.putdata of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1EE0>>
    board models Board getthum if type(c.putdata) : <class 'method'>
    board models Board getthum if c.putpalette : <bound method Image.putpalette of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1EF8>>
    board models Board getthum if type(c.putpalette) : <class 'method'>
    board models Board getthum if c.putpixel : <bound method Image.putpixel of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1F10>>
    board models Board getthum if type(c.putpixel) : <class 'method'>
    board models Board getthum if c.pyaccess : None
    board models Board getthum if type(c.pyaccess) : <class 'NoneType'>
    board models Board getthum if c.quantize : <bound method Image.quantize of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1F40>>
    board models Board getthum if type(c.quantize) : <class 'method'>
    board models Board getthum if c.readonly : 0
    board models Board getthum if type(c.readonly) : <class 'int'>
    board models Board getthum if c.reduce : <bound method Image.reduce of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1F70>>
    board models Board getthum if type(c.reduce) : <class 'method'>
    board models Board getthum if c.remap_palette : <bound method Image.remap_palette of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1F88>>
    board models Board getthum if type(c.remap_palette) : <class 'method'>
    board models Board getthum if c.resize : <bound method Image.resize of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1FA0>>
    board models Board getthum if type(c.resize) : <class 'method'>
    board models Board getthum if c.rotate : <bound method Image.rotate of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1FB8>>
    board models Board getthum if type(c.rotate) : <class 'method'>
    board models Board getthum if c.save : <bound method Image.save of <PIL.Image.Image image mode=RGB size=384x193 at 0x11B1FD0>>
    board models Board getthum if type(c.save) : <class 'method'>
    board models Board getthum if c.seek : <bound method Image.seek of <PIL.Image.Image image mode=RGB size=384x193 at 0xE295D78>>
    board models Board getthum if type(c.seek) : <class 'method'>
    board models Board getthum if c.show : <bound method Image.show of <PIL.Image.Image image mode=RGB size=384x193 at 0xE2DE028>>
    board models Board getthum if type(c.show) : <class 'method'>
    board models Board getthum if c.size : (384, 193)
    board models Board getthum if type(c.size) : <class 'tuple'>
    board models Board getthum if c.split : <bound method Image.split of <PIL.Image.Image image mode=RGB size=384x193 at 0xE2DE058>>
    board models Board getthum if type(c.split) : <class 'method'>
    board models Board getthum if c.tell : <bound method Image.tell of <PIL.Image.Image image mode=RGB size=384x193 at 0xE2DE070>>
    board models Board getthum if type(c.tell) : <class 'method'>
    board models Board getthum if c.thumbnail : <bound method Image.thumbnail of <PIL.Image.Image image mode=RGB size=384x193 at 0xE2DE088>>
    board models Board getthum if type(c.thumbnail) : <class 'method'>
    board models Board getthum if c.tobitmap : <bound method Image.tobitmap of <PIL.Image.Image image mode=RGB size=384x193 at 0xE2DE0A0>>
    board models Board getthum if type(c.tobitmap) : <class 'method'>
    board models Board getthum if c.tobytes : <bound method Image.tobytes of <PIL.Image.Image image mode=RGB size=384x193 at 0xE2DE0B8>>
    board models Board getthum if type(c.tobytes) : <class 'method'>
    board models Board getthum if c.toqimage : <bound method Image.toqimage of <PIL.Image.Image image mode=RGB size=384x193 at 0xE2DE0D0>>
    board models Board getthum if type(c.toqimage) : <class 'method'>
    board models Board getthum if c.toqpixmap : <bound method Image.toqpixmap of <PIL.Image.Image image mode=RGB size=384x193 at 0xE2DE0E8>>
    board models Board getthum if type(c.toqpixmap) : <class 'method'>
    board models Board getthum if c.transform : <bound method Image.transform of <PIL.Image.Image image mode=RGB size=384x193 at 0xE2DE100>>
    board models Board getthum if type(c.transform) : <class 'method'>
    board models Board getthum if c.transpose : <bound method Image.transpose of <PIL.Image.Image image mode=RGB size=384x193 at 0xE2DE118>>
    board models Board getthum if type(c.transpose) : <class 'method'>
    board models Board getthum if c.verify : <bound method Image.verify of <PIL.Image.Image image mode=RGB size=384x193 at 0xE2DE130>>
    board models Board getthum if type(c.verify) : <class 'method'>
    board models Board getthum if c.width : 384
    board models Board getthum if type(c.width) : <class 'int'>
    board models Board getthum if c.format : None
    board models Board getthum if type(c.format) : <class 'NoneType'>
    board models Board getthum if c.getdata : <bound method Image.getdata of <PIL.Image.Image image mode=RGB size=384x193 at 0xE2DE148>>
    board models Board getthum if type(c.getdata) : <class 'method'>
    board models Board getthum if c.load : <bound method Image.load of <PIL.Image.Image image mode=RGB size=384x193 at 0xE2DE148>>
    board models Board getthum if type(c.load) : <class 'method'>
    '''
        
        
    

    def __str__(self):
        return str(self.id)+" "+str(self.name)