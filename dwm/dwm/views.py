
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User,Subscribe
from board.models import Board, File,Likey,Reply
from django.core.paginator import Paginator
# Create your views here.

def gotoindex(req) :
    return redirect("dwm:index")

def index(req):
    global User
    if not req.user.username == "" :
        if len(Subscribe.objects.filter(subscriber=User.objects.get(username=req.user.username)))>0:
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

            print()
                #if req.user.username 
            print("dwm views index if if req.user :",req.user)
            print("dwm views index if if req.user.username :",req.user.username)
            print("dwm views index if if req.user.username == None :",req.user.username == None) # False
            print("dwm views index if if req.user.username == "" :",req.user.username == "") # True
            print("dwm views index if if User.objects.get(username=req.user.username) :",User.objects.get(username=req.user.username))
            print("dwm views index if if Subscribe.objects.filter(subscriber=User.objects.get(username=req.user.username)) :",Subscribe.objects.filter(subscriber=User.objects.get(username=req.user.username)))
            print("dwm views index if if len(Subscribe.objects.filter(subscriber=User.objects.get(username=req.user.username))) :",len(Subscribe.objects.filter(subscriber=User.objects.get(username=req.user.username))))
            print("dwm views index len(Subscribe.objects.filter(subscriber=User.objects.get(username=req.user.username)))>0 :",len(Subscribe.objects.filter(subscriber=User.objects.get(username=req.user.username)))>0)
            if len(Subscribe.objects.filter(subscriber=User.objects.get(username=req.user.username)))>0:
                userops = User.objects.get(username=req.user.username)
                

                subops = Subscribe.objects.filter(subscriber=userops)
                print("dwm views index if if if subops :",subops)
                print("dwm views index if if if type(subops) :",type(subops))
                print("dwm views index if if if len(subops) :",len(subops))
                result_subops = Board.objects.filter(id=0)
                print("dwm views index if if if result_subops :",result_subops)
                
                for i in subops :
                    print("dwm views index if if if for i :",i)
                    print("dwm views index if if if for i.id :",i.id)
                    print("dwm views index if if if for i.subscriber :",i.subscriber)
                    print("dwm views index if if if for i.mainuser :",i.mainuser)

                    bi = Board.objects.filter(writerops=i.mainuser)
                    print("dwm views index if if if for bi :",bi)
                    print("dwm views index if if if for bi :",len(bi))
                    result_subops = result_subops.union(bi, all=True)
                    print("dwm views index if if if for result_subops :",result_subops)
                    print("dwm views index if if if for len(result_subops) :",len(result_subops))

                    
                likeies = Likey.objects.filter(mainuser=userops)
                print("dwm views index if if if likeies :",likeies)
                print("dwm views index if if if type(likeies) :",type(likeies))
                print("dwm views index if if if len(likeies) :",len(likeies))
                for i in likeies :
                    li = Board.objects.filter(id=i.likeyboard.id)
                    print("dwm views index if if if for li :",li)
                    print("dwm views index if if if for li :",len(li))
                    result_subops = result_subops.union(li,all=True)
                #result_subops = result_subops.union(likeies,all=True)
                
                result_subops = result_subops.order_by('-id')
                context = {
                    "showtbl" : True,      
                    "showsubs" : True,
                    "boardobj" : result_subops,
                    "subops" : subops,
                    "likeies" : likeies
                }
        else :
            context = {
            "showtbl" : False
        }
    else :
        context = {
            "showtbl" : False
        }

    return render(req,"dwm/index.html",context=context)


def join(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        userpassword = request.POST.get("upass")
        usercomment = request.POST.get("ucomm")
        useremail = request.POST.get("umail")
        usernickname = request.POST.get("unick")
        userpicture = request.FILES.get("upic")
        User.objects.create_user(username=username, password=userpassword, nickname=usernickname,comment=usercomment, email=useremail, photo=userpicture)
        return redirect("dwm:index")
    return render(request, "dwm/join.html")

def userlogin(req):
    if req.method == "POST":
        username = req.POST.get("uname")
        userpassword = req.POST.get("upass")
        
        userobj = User.objects.get(username=username)
        userobj = authenticate(username=username, password=userpassword,nickname=userobj.nickname,userid=userobj.id)
        if userobj:
            login(req, userobj)
            return redirect("dwm:index")
        else:
            pass 
    return render(req, "dwm/login.html")


def userlogout(req):
    logout(req)
    return redirect("dwm:index")

def mod(req) : 
    #req : request
    #tid : target id
    if req.method == "POST":
        tid = req.user.id
        userobj = User.objects.get(id=tid)
        # print("dwm views mod req.session :",req.session)
        # print("dwm views mod tid :",tid)
        
        usernickname = req.POST.get("nickname")                                  
        usercomment = req.POST.get("ucomm")
        useremail = req.POST.get("umail")
        userpicture = req.FILES.get("upic")
        # print("dwm views mod usernickname :",usernickname)
        # print("dwm views mod type(usernickname) :",usernickname)
        # print("dwm views mod usercomment :",usercomment)
        # print("dwm views mod type(usercomment) :",usercomment)
        # print("dwm views mod useremail :",useremail)
        # print("dwm views mod type(useremail) :",useremail)
        # print("dwm views mod userpicture :",userpicture)
        # print("dwm views mod type(userpicture) :",userpicture)

        userobj.nickname = usernickname
        userobj.comment = usercomment
        userobj.email = useremail

        if not userpicture == None :
            userobj.photo = userpicture
        userobj.save()
        

        return redirect("dwm:index")
    return render(req, "dwm/mod.html")



