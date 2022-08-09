from audioop import reverse
from re import T
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Board
from django.utils import timezone
from django.http import HttpResponseRedirect
from dwm.models import User
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from config import settings
import os
from django.http import HttpResponse 
from django.http import Http404 
# Create your views here.

def gotoindex(req) :
    return redirect("board:index")
    
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
    writers = BoardObj.values('writername')
    writers = writers.distinct()
    #print("board views index writers :",writers)
    #print("board views index type(writers) :",type(writers))
    writersname = []
    for i in writers : 
        #print("i : ",i)
        #print("type(i) : ",type(i))
        writersname.append(i['writername'])
    writersname = set(writersname)
    writersname = list(writersname)
    #print("board views index writersname :",writersname)
    #print("board views index writersname.values() :",writersname.values())
    writerphotos = []
    for i in range(len(writersname)) :
        #print("board views index for i writersname[i] :",writersname[i])
        tempphs = User.objects.get(username=writersname[i])
        #print("board views index for i tempphs 1 :",tempphs)
        #print("board views index for i type(tempphs) 1 :",type(tempphs))
        tempphs = User.getphoto(tempphs)
        #print("board views index for i tempphs 2 :",tempphs)
        #print("board views index for i type(tempphs) 2 :",type(tempphs))
        #print("board views index for i {writersname[i]:tempphs} :",{writersname[i]:tempphs})
        
        writerphotos.append({writersname[i]:tempphs})
    print("board views index writerphotos :",writerphotos)
    #print("board views index type(writerphotos) :",type(writerphotos))

    PageData = Paginator(BoardObj, 5)
    BoardObj = PageData.get_page(Page)
    context = {
        "boardobj" : BoardObj,
        "writerphotos" : writerphotos
    }
    return render(req, "board/index.html", context)

def create(req):
    if req.method == "POST":
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            username = req.user.username
            usernickname = req.user.nickname
            thumbnail = req.FILES.get("thumbnail")
            name = req.POST.get("name")
            comment = req.POST.get("comment")
            print("board views create post")
            print("username :",username)
            print("usernickname :",usernickname)
            print("thumbnail :",thumbnail)
            print("name :",name)
            print("comment :",comment)
            Board(name=name, comment=comment, writername=username,thumbnail=thumbnail,writernick=usernickname,credate=timezone.now()).save()
            return redirect("board:index")
    
    elif req.method == "GET":
        print("board views create get")
        print("board views create get req.user.username :",req.user.username)
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            return render(req, "board/create.html")


def mod(req, tr):
    if req.method == "POST":
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            BoardObj = Board.objects.get(id=tr)
            # print("board views mod BoardObj.writername :",BoardObj.writername)
            # print("board views mod req.user.username :",req.user.username)
            if BoardObj.writername == req.user.username :

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
            print("board views mod BoardObj.writername :",BoardObj.writername)
            print("board views mod req.user.username :",req.user.username)
            if BoardObj.writername == req.user.username :
                print("board views mod over if")
                context = {
                    "boardobj" : BoardObj
                }
                return render(req, "board/mod.html",context)


def delete(req, tr):
    if req.method == "GET":
        print("board views create get")
        print("board views create get req.user.username :",req.user.username)
        
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            r = Board.objects.get(id=tr)
            print("board views mod r.writername :",r.writername)
            print("board views mod req.user.username :",req.user.username)
            if r.writername == req.user.username :
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
    
    context = {
        "boardobj" : BoardObj
    }
    return render(req, "board/detail.html",context)

def down(req):
    print("board views down entered")
    downtarget = req.GET.get("downtarget","/media/no.jpg")
    print("board views down path :",downtarget)
    file_path = os.path.join(str(settings.MEDIA_ROOT)+"/boardpic", downtarget)
    print("board views down file_path :",file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404