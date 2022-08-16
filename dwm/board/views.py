from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Board
from .models import Reply
from django.utils import timezone
from dwm.models import User
from PIL import Image
from config import settings
import os
from django.http import HttpResponse 
from django.http import Http404 
from django.core.files import File
# Create your views here.

def gotoindex(req) :
    return redirect("board:index")


def create(req):
    if req.method == "POST":
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            
            username = req.user.username
            usernickname = req.user.nickname
            boardfile = req.FILES.get("file")
            name = req.POST.get("name")
            comment = req.POST.get("comment")
            print("board views create if else username :",username)
            print("board views create if else usernickname :",usernickname)
            print("board views create if else boardfile :",boardfile) #thumbnail : 20200927_161805.png
            print("board views create if else type(boardfile) :",type(boardfile)) #thumbnail : 20200927_161805.png
            print("board views create if else name :",name)
            print("board views create if else comment :",comment)
            creatinguser = User.objects.get(username=username)
            b = Board()
            b.name = name
            b.writerops = creatinguser
            b.comment = comment
            b.boardfile = boardfile
            print("board views create if else b.boardfile :",b.boardfile) #thumbnail : 20200927_161805.png
            print("board views create if else type(b.boardfile) :",type(b.boardfile)) #thumbnail : 20200927_161805.png
            b.credate = timezone.now()
            b.save()
            print("board views create if else b :",b)
            print("board views create if else type(b) :",type(b))
            print("board views create if else b.id :",b.id)


            print("str(boardfile) :",str(boardfile))
            print("str(boardfile).split('.') :",str(boardfile).split('.'))
            print("str(boardfile).split('.')[-1] :",str(boardfile).split('.')[-1])
            print("str(boardfile).split('.')[-1] in ['png','jpg','jpeg']  :",str(boardfile).split('.')[-1] in ['png','jpg','jpeg'] )

            if str(boardfile).split('.')[-1] in ['png','jpg','jpeg'] :

                change_path=str(settings.MEDIA_ROOT)+'\low\\boardpic\\'
                print("baord views create b :",b)
                print("baord views create type(b) :",type(b))
                print("baord views create b.getfilename() :",b.getfilename())
                print("baord views create type(b.getfilename()) :",type(b.getfilename()))
                filename = str(b.getfilename()).split("/")[-1]
                print("baord views create filename :",filename)
                original_path = str(settings.MEDIA_ROOT)+'\\boardpic\\'
                file = original_path + filename


                print("baord views create file :",file)
                print("baord views create type(file) :",type(file))

                img = Image.open(file,'r')
                print("baord view try im 1")
                img_resize = img.resize((int(img.width / 5), int(img.height / 5)))
                img_resize.save(change_path+filename, qualty=30)
                print("baord view try im 2")
                print("baord view try img_resize :",img_resize)
                print("baord view try type(img_resize) :",type(img_resize))

                print("baord view try img :",img)
                print("baord view try type(img) :",type(img))
                b.thumbnail = str(change_path+filename)

            b.save()
            print("baord view try im 3")
            print("baord view try im 4")



            return redirect("board:index")
    
    elif req.method == "GET":
        print("board views create get")
        print("board views create get req.user.username :",req.user.username)
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            return render(req, "board/create.html")

def index(req):
    global User
    Page = req.GET.get("page",1)
    CategoryName = req.GET.get("cate" ,"")
    KeyWordName = req.GET.get("kw","")
    Order = req.GET.get("o","di")

    #Page : 페이지네이터가 나눈 페이지의 순번 : The order of the pages divided by 'Paginator'

    #CategoryName : 카테고리를 이용한 검색을 했을때, 이 단어 또는 문장 : When you search using categories, this word or sentence
    #sub : subject : Search by Name : 작성된 객체의 이름(제목)으로 검색합니다.
    #wri : writer nick name : Search by Writer Nick Name : 작성자의 별명으로 검색합니다.
    #com : comment : Search by Comment : 작성된 내용물의 코멘트 내용의 포함된 객체들을 검색합니다.

    #KeyWordName : 카테고리를 이용한 검색을 했을때, 이 단어 또는 문장 : When you search using categories, this word or sentence

    #Order : 일련번호(아이디)나 생성순서 등의 기준을 둔 내림차순과 오름차순의 구분 데이터 : Separated data in descending and ascending order based on serial number (ID) or generation order
    #ud : upper date : 생성일자 기준 오름차순 : Ascending order based on creation date
    #dd : downer date : 생성일자 기준 내림차순 : In descending order based on generation date
    #ui : upper id : 아이디 기준 오름차순 : Ascending by ID
    #di : downer id : 아이디 기준 내림차순 : Based on ID, descending order

    #BoardObj : board 앱에서 만들어진 models의 Board 클래스에 기반을 둔 다목적 객체. : A multipurpose object based on the Board class of models created in the board app.

    #writers : 출력해야하는 (한 페이지) 목록의 모든 작성자들의 정보 : Information for all authors of the (one page) list that needs to be printed
    #writersname : 출력해야하는 (한 페이지) 목록의 모든 작성자들의 이름(WriterNickName) : Name (WriterNickName) of all authors of the (one page) list that needs to be printed
    #writerphotos : 출력해야하는 (한 페이지) 목록의 모든 작성자들의 프로필 사진의 주소 : The address of the profile picture of all authors in the (one page) list that needs to be printed

    #PageData : 출력할 수 있을 가능성이 있는 모든 객체들의 모음 : A collection of all objects that are likely to be output
    #BoardObj : 한 페이지에 반드시 출력해야할 객체들의 모음 : A collection of objects that must be printed on a page

    if KeyWordName:
        if CategoryName == "sub":
            BoardObj = Board.objects.filter(subject__startswith=KeyWordName)
        elif CategoryName == "wri":
            try:
                from dwm.models import User
                u = User.objects.get(username=KeyWordName)
                BoardObj = Board.objects.filter(writername=u)
            except:
                BoardObj = Board.objects.none()
        elif CategoryName == "com":
            BoardObj = Board.objects.filter(comment__contains=KeyWordName)
    else:
        BoardObj = Board.objects.all()

    if Order == "ud":
        BoardObj = BoardObj.order_by('credate')
    elif Order == "dd" :
        BoardObj = BoardObj.order_by('-credate')
    if Order == "ui":
        BoardObj = BoardObj.order_by('id')
    elif Order == "di" :
        BoardObj = BoardObj.order_by('-id')
    
    
    PageData = Paginator(BoardObj, 5)
    BoardObj = PageData.get_page(Page)
    context = {
        "boardobj" : BoardObj
    }
    return render(req, "board/index.html", context)



def mod(req, tr):
    if req.method == "POST":
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            BoardObj = Board.objects.get(id=tr)
            # print("board views mod BoardObj.writername :",BoardObj.writername)
            # print("board views mod req.user.username :",req.user.username)
            if BoardObj.writerops.username == req.user.username :

                name = req.POST.get("name")
                thumbnail = req.FILES.get("thumbnail")
                comment = req.POST.get("comment")
                # print("board views mod if if name :",name)
                # print("board views mod if if thumbnail :",thumbnail)
                # print("board views mod if if comment :",comment)
                if not thumbnail == None :
                    BoardObj.thumbnail = thumbnail
                    #print("board views mod if if if changethumnail? : yes")
                BoardObj.name = name
                BoardObj.comment = comment
                BoardObj.save()
                BoardObj = Board.objects.get(id=tr)
                context = {
                    "boardobj" : BoardObj
                }
                return render(req, "board/detail.html",context)
    
    elif req.method == "GET":
        print("board views create get")
        print("board views create get req.user.username :",req.user.username)
        
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            BoardObj = Board.objects.get(id=tr)
            print("board views mod BoardObj.writerops.username :",BoardObj.writerops.username)
            print("board views mod req.user.username :",req.user.username)
            if BoardObj.writerops.username == req.user.username :
                print("board views mod over if")
                context = {
                    "boardobj" : BoardObj
                }
                return render(req, "board/mod.html",context)

def reply(req, tr):
    if req.method == "POST":
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            reply_comment = req.POST.get("reply_comment")
            if reply_comment == None :
                reply_comment = ""
            print("board views reply post")
            username = req.user.username
            replyinguser = User.objects.get(username=username)
            Reply(comment_id=tr,reply_writerops=replyinguser,reply_comment=reply_comment,credate=timezone.now()).save()
            return redirect("/board/detail/"+tr)
    elif req.method == "GET":
        return redirect("board:index")

def replydel(req, replytr,boardtr):
    if req.method == "GET":
        print("board views replydel get")
        print("board views replydel get req.user.username :",req.user.username)
        
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            r = Reply.objects.get(id=replytr)
            print("board views mod r.reply_writerops.username :",r.reply_writerops.username)
            print("board views mod req.user.username :",req.user.username)
            if r.reply_writerops.username == req.user.username :
                r.delete()
            return redirect("/board/detail/"+boardtr)

def delete(req, tr):
    if req.method == "GET":
        print("board views delete get")
        print("board views delete get req.user.username :",req.user.username)
        
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            r = Board.objects.get(id=tr)
            print("board views mod r.writerops.username :",r.writerops.username)
            print("board views mod req.user.username :",req.user.username)
            if r.writerops.username == req.user.username :
                r.delete()
                return redirect("board:index")


def detail(req, tr) :
    print("board views detail tr :",tr)
    #tr : target raw
    BoardObj = Board.objects.get(id=tr)
    #print("board views detail BoardObj :",BoardObj)
    #print("board views detail type(BoardObj) :",type(BoardObj))
    #print("board views detail BoardObj.id :",BoardObj.id)
    #print("board views detail BoardObj.writernick :",BoardObj.writernick)
    #print("board views detail BoardObj.credate :",BoardObj.credate)
    #print("board views detail BoardObj.name :",BoardObj.name)
    #print("board views detail BoardObj.thumbnail :",BoardObj.thumbnail)
    #print("board views detail BoardObj.comment :",BoardObj.comment)
    BoardObj.hits = BoardObj.hits+1
    BoardObj.save()
    ReplyObj = Reply.objects.filter(comment_id=tr)
    ReplyObj = ReplyObj.order_by('-id')
    print("board views detail ReplyObj 2:",ReplyObj)
    context = {
        "boardobj" : BoardObj,
        "replyobj" : ReplyObj
    }
    print("board views detail tried t")
    return render(req, "board/detail.html",context)

def down(req): #media board pic
    print("board views down entered")
    downtarget = req.GET.get("downtarget","/media/no.jpg")
    print("board views down downtarget :",downtarget)
    print("board views down type(downtarget) :",type(downtarget))
    print("board views down str(settings.MEDIA_ROOT) :",str(settings.MEDIA_ROOT))
    
    file_path = os.path.join(str(settings.MEDIA_ROOT)+"", downtarget)
    print("board views down file_path :",file_path)
    try :
        print("board views down try")
        return filedownload(file_path)
    except :
        print("board views down except")
        print("board views down except str(downtarget) :",str(downtarget))
        print("board views down except str(downtarget).split('/') :",str(downtarget).split('/'))
        print("board views down except str(downtarget).split('/')[2:] :",str(downtarget).split('/')[2:])
        print("board views down except '\\'.join(str(downtarget).split('/')[2:]) :",'\\'.join(str(downtarget).split('/')[2:]))
        downtarget = '\\'.join(str(downtarget).split('/')[2:])
        print("board views down except downtarget :",downtarget)
        print("board views down except type(downtarget) :",type(downtarget))
        file_path = str(settings.MEDIA_ROOT)+"\\"+str(downtarget)
        print("board views down except file_path :",file_path)
        return filedownload(file_path)
def filedownload(file_path) :
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            endpart = str(file_path).split(".")[-1]
            print("board views filedownload if with endpart :",endpart)
            if endpart == 'txt' :
                response = HttpResponse(file.read(), content_type="application/txt; charset=utf-8")
            elif endpart == 'zip' :
                response = HttpResponse(file.read(), content_type="application/x-zip-compressed; charset=utf-8")
            else :
                response = HttpResponse(file.read(), content_type="application/vnd.ms-excel; charset=utf-8")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def change_img_qualty(targetid, change_path=str(settings.MEDIA_ROOT)+'\low\\boardpic\\', qualty=30):
    """
    Change Image Qualty
    :param original_path: 원본 경로
    :param change_path: 변경 후 새롭게 저장될 경로
    :param qualty: Qualty(품질) 퍼센트(기본 : 85%)
    :return:
    """
    print("baord view change_img_qualty settings.MEDIA_ROOT :",settings.MEDIA_ROOT)
    print("baord view change_img_qualty settings.MEDIA_URL :",settings.MEDIA_URL)
    print("baord view change_img_qualty targetid :",targetid)
    print("baord view change_img_qualty change_path :",change_path)
    b = Board.objects.get(id=targetid)
    print("baord view change_img_qualty b :",b)
    print("baord view change_img_qualty type(b) :",type(b))
    print("baord view change_img_qualty b.getthum() :",b.getthum())
    print("baord view change_img_qualty type(b.getthum()) :",type(b.getthum()))
    filename = str(b.getthum()).split("/")[-1]
    print("baord view change_img_qualty filename :",filename)
    original_path = str(settings.MEDIA_ROOT)+'\\boardpic\\'
    file = original_path + filename

    print("baord view change_img_qualty file :",file)
    print("baord view change_img_qualty type(file) :",type(file))
    continu = input("enter anything for keep going\n")
    try:
        img = Image.open(file)
        print("baord view try im 1")
        img_resize = img.resize((int(img.width / 5), int(img.height / 5)))
        img_resize.save(change_path+filename, qualty=qualty)
        print("baord view try im 2")
    except Exception as e:
        print("+ 실패 : {fail}".format(fail=file))



