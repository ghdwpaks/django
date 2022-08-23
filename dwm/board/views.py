from ast import Break, Pass, Sub
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Board, File,Likey
from .models import Reply
from django.utils import timezone as Timezone
from dwm.models import User, Subscribe
from PIL import Image
from config import settings
import os
from django.http import HttpResponse 
from django.http import Http404 
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
            name = req.POST.get("name")
            comment = req.POST.get("comment")
            public = req.POST.get("public")
            print("board views create if else public :",public)
            print("board views create if else type(public) :",type(public))
            if public == "able" :
                print("board views create if else if public = True")
                public = True
            elif public == "disable" :
                print("board views create if else if public = False")
                public = False
            # print("board views create if else username :",username)
            # print("board views create if else usernickname :",usernickname)20200927_161805.png
            # print("board views create if else name :",name)
            # print("board views create if else comment :",comment)
            creatinguser = User.objects.get(username=username)
            b = Board()
            b.name = name
            b.writerops = creatinguser
            b.comment = comment
            b.credate = Timezone.now()
            b.public = public
            b.save()
            print("board views create if else b :",b)
            print("board views create if else type(b) :",type(b))
            print("board views create if else b.id :",b.id)
            for img in req.FILES.getlist('files'):
                print("board views create if else for img : ",img)
                print("board views create if else for str(img) : ",str(img))
                photo = File()
                photo.boardops = b
                photo.image = img
                photo.save()
                print("board views create if else for if str(img) :",str(img))
                print("board views create if else for if str(img).split('.') :",str(img).split('.'))
                print("board views create if else for if str(img).split('.')[-1] :",str(img).split('.')[-1])
                if str(img).split(".")[-1] in ['png','jpg','jpeg'] :
                    print("board views create if else for if if")
                    change_path=str(settings.MEDIA_ROOT)+'\low\\boardpic\\'
                    original_path = str(settings.MEDIA_ROOT)+'\\boardpic\\'
                    filename = str(photo.image).split("/")[-1]
                    file = original_path + filename
                    img = Image.open(file,'r')
                    img_resize = img.resize((int(img.width / 5), int(img.height / 5)))
                    print("board views create if else for if if change_path :",change_path)
                    print("board views create if else for if if original_path :",original_path)
                    print("board views create if else for if if filename :",filename)
                    print("board views create if else for if if type(filename) :",type(filename))
                    print("board views create if else for if if file :",file)
                    print("board views create if else for if if type(file) :",type(file))
                    print("board views create if else for if if img :",img)
                    print("board views create if else for if if type(img) :",type(img))
                    print("board views create if else for if if 1 img_resize :",img_resize)
                    print("board views create if else for if if 1 type(img_resize) :",type(img_resize))
                    img_resize.save(change_path+filename, qualty=30)
                    print("board views create if else for if if 2 img_resize :",img_resize)
                    print("board views create if else for if if 2 type(img_resize) :",type(img_resize))
                    b.thumbnail = str(change_path+filename)
                    b.save()
            # print("baord view try im 3")
            # print("baord view try im 4")
            '''
            if str(boardfile).split('.')[-1] in ['png','jpg','jpeg'] :
                change_path=str(settings.MEDIA_ROOT)+'\low\\boardpic\\'
                filename = str(b.getfilename()).split("/")[-1]
                original_path = str(settings.MEDIA_ROOT)+'\\boardpic\\'
                file = original_path + filename
                img = Image.open(file,'r')
                img_resize = img.resize((int(img.width / 5), int(img.height / 5)))
                img_resize.save(change_path+filename, qualty=30)
                b.thumbnail = str(change_path+filename)
            '''



            return redirect("board:index")
    
    elif req.method == "GET":
        # print("board views create get")
        # print("board views create get req.user.username :",req.user.username)
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            return render(req, "board/create.html")

def index(req):
    global User
    page = req.GET.get("page",1)
    categoryname = req.GET.get("category" ,"")
    keywordname = req.GET.get("keyword","")
    orber = req.GET.get("order","di")

    #page : 페이지네이터가 나눈 페이지의 순번 : The order of the pages divided by 'Paginator'

    #categoryname : 카테고리를 이용한 검색을 했을때, 이 단어 또는 문장 : When you search using categories, this word or sentence
    #sub : subject : Search by Name : 작성된 객체의 이름(제목)으로 검색합니다.
    #wri : writer nick name : Search by Writer Nick Name : 작성자의 별명으로 검색합니다.
    #com : comment : Search by Comment : 작성된 내용물의 코멘트 내용의 포함된 객체들을 검색합니다.

    #keywordname : 카테고리를 이용한 검색을 했을때, 이 단어 또는 문장 : When you search using categories, this word or sentence

    #Order : 일련번호(아이디)나 생성순서 등의 기준을 둔 내림차순과 오름차순의 구분 데이터 : Separated data in descending and ascending order based on serial number (ID) or generation order
    #ud : upper date : 생성일자 기준 오름차순 : Ascending order based on creation date
    #dd : downer date : 생성일자 기준 내림차순 : In descending order based on generation date
    #ui : upper id : 아이디 기준 오름차순 : Ascending by ID
    #di : downer id : 아이디 기준 내림차순 : Based on ID, descending order

    #boardobj : board 앱에서 만들어진 models의 Board 클래스에 기반을 둔 다목적 객체. : A multipurpose object based on the Board class of models created in the board app.

    #writers : 출력해야하는 (한 페이지) 목록의 모든 작성자들의 정보 : Information for all authors of the (one page) list that needs to be printed
    #writersname : 출력해야하는 (한 페이지) 목록의 모든 작성자들의 이름(WriterNickName) : Name (WriterNickName) of all authors of the (one page) list that needs to be printed
    #writerphotos : 출력해야하는 (한 페이지) 목록의 모든 작성자들의 프로필 사진의 주소 : The address of the profile picture of all authors in the (one page) list that needs to be printed

    #pagedata : 출력할 수 있을 가능성이 있는 모든 객체들의 모음 : A collection of all objects that are likely to be output
    #boardobj : 한 페이지에 반드시 출력해야할 객체들의 모음 : A collection of objects that must be printed on a page

    if keywordname:
        if categoryname == "sub":
            boardobj = Board.objects.filter(subject__startswith=keywordname)
        elif categoryname == "wri":
            try:
                u = User.objects.get(username=keywordname)
                boardobj = Board.objects.filter(writername=u)
            except:
                boardobj = Board.objects.none()
        elif categoryname == "com":
            boardobj = Board.objects.filter(comment__contains=keywordname)
    else:
        boardobj = Board.objects.all()

    if orber == "ud":
        boardobj = boardobj.order_by('credate')
    elif orber == "dd" :
        boardobj = boardobj.order_by('-credate')
    if orber == "ui":
        boardobj = boardobj.order_by('id')
    elif orber == "di" :
        boardobj = boardobj.order_by('-id')
    
    
    pagedata = Paginator(boardobj, 5)
    boardobj = pagedata.get_page(page)
    print()
    #if req.user.username 
    print("board views index req.user :",req.user)
    print("board views index req.user.username :",req.user.username)
    print("board views index req.user.username == None :",req.user.username == None) # False
    print("board views index req.user.username == "" :",req.user.username == "") # True
    if not req.user.username == "" and len(Subscribe.objects.filter(subscriber=User.objects.get(username=req.user.username)))>0:
        userops = User.objects.get(username=req.user.username)
        subops = Subscribe.objects.filter(subscriber=userops)
        print("board views index subops :",subops)
        print("board views index type(subops) :",type(subops))
        print("board views index len(subops) :",len(subops))
        likeies = Likey.objects.filter(mainuser=userops)
        print("board views index likeies :",likeies)
        print("board views index type(likeies) :",type(likeies))
        print("board views index len(likeies) :",len(likeies))
        context = {
            "showsubs" : True,
            "boardobj" : boardobj,
            "subops" : subops,
            "likeies" : likeies
        }
    else :
        context = {
            "showsubs" : False,
            "boardobj" : boardobj
        }
    
    return render(req, "board/index.html", context)



def mod(req, tr):
    if req.method == "POST":
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            boardobj = Board.objects.get(id=tr)
            # print("board views mod boardobj.writername :",boardobj.writername)
            # print("board views mod req.user.username :",req.user.username)
            if boardobj.writerops.username == req.user.username :
                
                name = req.POST.get("name")
                thumbnail = req.FILES.get("thumbnail")
                comment = req.POST.get("comment")
                public = req.POST.get("public")
                if public == "able" : public = True
                elif public == "disable" : public = False
                # print("board views mod if if name :",name)
                # print("board views mod if if thumbnail :",thumbnail)
                # print("board views mod if if comment :",comment)
                if not thumbnail == None :
                    boardobj.thumbnail = thumbnail
                    #print("board views mod if if if changethumnail? : yes")
                boardobj.name = name
                boardobj.comment = comment
                boardobj.public = public
                boardobj.save()
                
                for img in req.FILES.getlist('files'):
                    print("board views mod if else if for img : ",img)
                    print("board views mod if else if for str(img) : ",str(img))
                    photo = File()
                    photo.boardops = boardobj
                    photo.image = img
                    photo.save()
                    if str(img).split(".")[-1] in ['png','jpg','jpeg'] :
                        print("board views create if else for if if")
                        change_path=str(settings.MEDIA_ROOT)+'\low\\boardpic\\'
                        original_path = str(settings.MEDIA_ROOT)+'\\boardpic\\'
                        filename = str(photo.image).split("/")[-1]
                        file = original_path + filename
                        img = Image.open(file,'r')
                        img_resize = img.resize((int(img.width / 5), int(img.height / 5)))
                        print("board views create if else for if if change_path :",change_path)
                        print("board views create if else for if if original_path :",original_path)
                        print("board views create if else for if if filename :",filename)
                        print("board views create if else for if if type(filename) :",type(filename))
                        print("board views create if else for if if file :",file)
                        print("board views create if else for if if type(file) :",type(file))
                        print("board views create if else for if if img :",img)
                        print("board views create if else for if if type(img) :",type(img))
                        print("board views create if else for if if 1 img_resize :",img_resize)
                        print("board views create if else for if if 1 type(img_resize) :",type(img_resize))
                        img_resize.save(change_path+filename, qualty=30)
                        print("board views create if else for if if 2 img_resize :",img_resize)
                        print("board views create if else for if if 2 type(img_resize) :",type(img_resize))
                        boardobj.thumbnail = str(change_path+filename)
                        boardobj.save()
                
                files = File.objects.filter(boardops=boardobj)
                if len(files) == 0 :
                    boardobj.thumbnail = None
                    boardobj.save()
                print("board views mod if else if files :",files)
                
                print("board views mod if else if type(files) :",type(files))
                
                boardobj = Board.objects.get(id=tr)
                replyobj = Reply.objects.filter(comment_id=tr)
                replyobj = replyobj.order_by('-id')
                context = {
                    "boardobj" : boardobj,
                    "replyobj" : replyobj,
                    "files": files
                }
                return render(req, "board/detail.html",context)
    
    elif req.method == "GET":
        # print("board views create get")
        # print("board views create get req.user.username :",req.user.username)
        
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            boardobj = Board.objects.get(id=tr)
            # print("board views mod boardobj.writerops.username :",boardobj.writerops.username)
            # print("board views mod req.user.username :",req.user.username)
            if boardobj.writerops.username == req.user.username :
                # print("board views mod over if")
                files = File.objects.filter(boardops=boardobj)
                context = {
                    "boardobj" : boardobj,
                    "files": files
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
            # print("board views reply post")
            username = req.user.username
            replyinguser = User.objects.get(username=username)
            Reply(comment_id=tr,reply_writerops=replyinguser,reply_comment=reply_comment,credate=Timezone.now()).save()
            return redirect("/board/detail/"+tr)
    elif req.method == "GET":
        return redirect("board:index")

def replydel(req, replytr,boardtr):
    if req.method == "GET":
        # print("board views replydel get")
        # print("board views replydel get req.user.username :",req.user.username)
        
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            r = Reply.objects.get(id=replytr)
            # print("board views mod r.reply_writerops.username :",r.reply_writerops.username)
            # print("board views mod req.user.username :",req.user.username)
            if r.reply_writerops.username == req.user.username : r.delete()
            return redirect("/board/detail/"+boardtr)
def imgdel(req,imgid,boardtr) :
    if req.method == "GET":
        
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            r = File.objects.get(id=imgid)
            if r.boardops.writerops.username == req.user.username :
                r.delete()
                return redirect("/board/mod/"+boardtr)

def delete(req, tr):
    if req.method == "GET":
        # print("board views delete get")
        # print("board views delete get req.user.username :",req.user.username)
        
        if req.user.username == None or req.user.username == "" :
            return redirect("board:index")
        else :
            r = Board.objects.get(id=tr)
            # print("board views mod r.writerops.username :",r.writerops.username)
            # print("board views mod req.user.username :",req.user.username)
            if r.writerops.username == req.user.username :
                r.delete()
                return redirect("board:index")


def detail(req, tr) :
    print("board views detail tr :",tr)
    #tr : target raw
    boardobj = Board.objects.get(id=tr)
    print("board views detail boardobj :",boardobj)
    print("board views detail type(boardobj) :",type(boardobj))
    print("board views detail boardobj.id :",boardobj.id)
    print("board views detail boardobj.credate :",boardobj.credate)
    print("board views detail boardobj.name :",boardobj.name)
    print("board views detail boardobj.thumbnail :",boardobj.thumbnail)
    print("board views detail boardobj.comment :",boardobj.comment)
    files = File.objects.filter(boardops=boardobj)
    print("board views detail files :",files)
    print("board views detail type(files) :",type(files))
    try :
        print("board views detail try files.boardops :",files.boardops)
        print("board views detail try type(files.boardops) :",type(files.boardops))
        print("board views detail try files.image :",files.image)
        print("board views detail try type(files.image) :",type(files.image))
    except :
        print("error from board views detail except")
    boardobj.hits = boardobj.hits+1
    boardobj.save()
    # print("board views detail boardobj.public :",boardobj.public)
    # print("board views detail type(boardobj.public) :",type(boardobj.public))
    # print("board views detail boardobj.writerops.username :",boardobj.writerops.username)
    # print("board views detail type(boardobj.writerops.username) :",type(boardobj.writerops.username))
    # print("board views detail req.user.username :",req.user.username)
    # print("board views detail type(req.user.username) :",type(req.user.username))
    if boardobj.public == True :
        # print("board views detail if")
        pass
    elif boardobj.public == False and str(boardobj.writerops.username) == req.user.username:
        # print("board views detail elif 1")
        pass
    else :
        # print("board views detail else")
        return redirect("board:index")
        
    replyobj = Reply.objects.filter(comment_id=tr)
    replyobj = replyobj.order_by('-id')
    #print("board views detail ReplyObj 2:",replyobj)
    context = {
        "boardobj" : boardobj,
        "replyobj" : replyobj,
        "files": files
    }
    #print("board views detail tried t")
    return render(req, "board/detail.html",context)


def userdetail(req, tr) :
    #not get username by GET.
    #get board raw id first, and search in back.
    #use username only backend.
    print("board views detail tr :",tr)
    #tr : target raw
    page = req.GET.get("page",1)
    orber = req.GET.get("order","di")
    

    
    boardobj = Board.objects.get(id=tr)
    userops = User.objects.get(username=boardobj.writerops.username) #writer, detail target user, not me
    boardobj = Board.objects.filter(writerops=userops)
    if orber == "ud":
        boardobj = boardobj.order_by('credate')
    elif orber == "dd" :
        boardobj = boardobj.order_by('-credate')
    if orber == "ui":
        boardobj = boardobj.order_by('id')
    elif orber == "di" :
        boardobj = boardobj.order_by('-id')
    pagedata = Paginator(boardobj, 5)
    boardobj = pagedata.get_page(page)
    #if req.user.username 
    print("board views userdetail userops :",userops)
    print("board views userdetail req.user :",req.user)
    print("board views userdetail req.user.username :",req.user.username)
    print("board views userdetail req.user.username == None :",req.user.username == None) # False
    print("board views userdetail req.user.username == "" :",req.user.username == "") # True

    subscribing = False
    try :
        myops = User.objects.get(username=req.user.username)
        substargetuser = Subscribe.objects.filter(subscriber=myops) #내가 구독한 사람들 목록
        print("board views userdetail len(substargetuser) :",len(substargetuser))
        for i in substargetuser :
            if i.mainuser == userops :
                subscribing = True
                break
                
        print("board views userdetail subscribing :",subscribing)
    except :
        pass
    context = {
        "subscribing" : subscribing,
        "boardobj" : boardobj,
        "userops" : userops
    }
    return render(req, "board/userdetail.html", context)
    
def sub(req, userid) :
    print("board views sub ")
    subscribing = False
    if req.user.username == "" :
        return redirect("board:index")
    else :
        userops = User.objects.get(id=userid) #writer, detail target user, not me
        print("board views sub useropsv:",userops)
        myops = User.objects.get(username=req.user.username)
        print("board views sub myopsv:",myops)
        try : 
            subable = Subscribe.objects.get(mainuser=userops,subscriber=myops)
            print("board views sub else subable :",subable)
            print("board views sub else type(subable) :",type(subable))
            #unabled subscribe
            subscribing = True
        except :
            #able subscribe
            print("errored from board views sub if try received except")
            s = Subscribe()
            s.mainuser = userops
            s.subscriber = myops
            s.save()
            subscribing = True

    boardobj = Board.objects.filter(writerops=userops)
    boardobj = boardobj.order_by('-id')
    pagedata = Paginator(boardobj, 5)
    boardobj = pagedata.get_page(req.GET.get("page",1))
    context = {
        "subscribing" : subscribing,
        "boardobj" : boardobj,
        "userops" : userops
    }
    return render(req, "board/userdetail.html", context)


        
        
def unsub(req, userid) :
    print("board views sub ")
    subscribing = False
    if req.user.username == "" :
        return redirect("board:index")
    else :
        userops = User.objects.get(id=userid) #writer, detail target user, not me
        print("board views sub useropsv:",userops)
        myops = User.objects.get(username=req.user.username)
        print("board views sub myopsv:",myops)
        try : 
            subable = Subscribe.objects.get(mainuser=userops,subscriber=myops)
            print("board views sub else subable :",subable)
            print("board views sub else type(subable) :",type(subable))
            #abled unsubscribe
            subable.delete()
            subscribing = False
        except :
            #unable unsubscribe
            print("errored from board views sub if try received except")
            subscribing = False
    
    boardobj = Board.objects.filter(writerops=userops)
    boardobj = boardobj.order_by('-id')
    pagedata = Paginator(boardobj, 5)
    boardobj = pagedata.get_page(req.GET.get("page",1))
    context = {
        "subscribing" : subscribing,
        "boardobj" : boardobj,
        "userops" : userops
    }
    return render(req, "board/userdetail.html", context)


    userdetail(req,userid)
        


    


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
            # print("board views filedownload if with endpart :",endpart)
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
    # print("baord view change_img_qualty settings.MEDIA_ROOT :",settings.MEDIA_ROOT)
    # print("baord view change_img_qualty settings.MEDIA_URL :",settings.MEDIA_URL)
    # print("baord view change_img_qualty targetid :",targetid)
    # print("baord view change_img_qualty change_path :",change_path)
    b = Board.objects.get(id=targetid)
    # print("baord view change_img_qualty b :",b)
    # print("baord view change_img_qualty type(b) :",type(b))
    # print("baord view change_img_qualty b.getthum() :",b.getthum())
    # print("baord view change_img_qualty type(b.getthum()) :",type(b.getthum()))
    filename = str(b.getthum()).split("/")[-1]
    # print("baord view change_img_qualty filename :",filename)
    original_path = str(settings.MEDIA_ROOT)+'\\boardpic\\'
    file = original_path + filename

    # print("baord view change_img_qualty file :",file)
    # print("baord view change_img_qualty type(file) :",type(file))
    try:
        img = Image.open(file)
        # print("baord view try im 1")
        img_resize = img.resize((int(img.width / 5), int(img.height / 5)))
        img_resize.save(change_path+filename, qualty=qualty)
        # print("baord view try im 2")
    except Exception as e:

        # print("+ 실패 : {fail}".format(fail=file))
        pass


