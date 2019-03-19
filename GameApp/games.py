from django.http import HttpResponse
import os
from django.shortcuts import render,redirect
from GameApp.models import Game,User,News,Article
from GameApp.reptile import AddNews,GetWeatherInfo
from datetime import datetime
from GameApp.read import Read
from .forms import UserFrom,RegisterForm
from django.core.mail import send_mail,EmailMultiAlternatives


def login(request):
    if request.session.get('is_login',None):
        return redirect('/index/')
    if request.POST:
        login_form = UserFrom(request.POST)
        message = "用户账户/密码不能为空"
        if login_form.is_valid():
            u_name = login_form.cleaned_data['username']
            u_password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(user_name=u_name)
                print(user.user_name)
                if user.user_pwd == u_password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.user_name
                    return redirect('/index/')
                else:
                    message = "用户密码错误"
            except:
                message = "用户不存在"
        return render(request,'login.html',locals())
    login_form = UserFrom()
    return render(request,'login.html',locals())

# def login(request):
#     if request.POST:
#         u_name = request.POST["u_name"]
#         u_password = request.POST["u_pwd"]
#         if u_name and u_password:
#             try:
#                 user = User.objects.get(user_name=u_name)
#                 print(user.user_name)
#                 if user.user_pwd == u_password:
#                     return redirect('/index/')
#                 else:
#                     msg = "用户密码错误"
#             except:
#                 msg = "用户不存在"
#         else:
#             msg = "用户账户/密码不能为空"
#         return render(request, 'login.html', {'message': msg})
#     return render(request,'login.html')
def logout(request):
    if not request.session.get('is_login',None):
        return redirect("/login/")
    request.session.flush()
    return redirect("/login/")


def regiter(request):
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请完善您填写的信息"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:
                message = "两次输入的密码不一致"
                return render(request,'register.html',locals())
            else:
                same_name = User.objects.filter(user_name=username)
                if same_name:
                    message = "用户名已被注册，请重新填写！"
                    return render(request,'register.html',locals())
                same_email = User.objects.filter(user_email=email)
                if same_email:
                    message = "邮箱已经被注册，请重新填写！"
                    return render(request, 'register.html', locals())
                new_user = User.objects.create()
                new_user.user_name = username
                new_user.user_pwd = password1
                new_user.user_email = email
                new_user.user_sex = sex
                new_user.save()
                sendemail(request,email,username)
                return redirect("/login/")
    register_form = RegisterForm()
    return render(request,'register.html',locals())


def selectAll(request):
    game_list = Game.objects.all()
    return render(request, 'index.html', {'games':game_list})

def search_game(request):
    request.encoding = 'utf-8'
    try:
        txt = request.GET['txt_search']
        if txt == '':
            game_list = Game.objects.all()
        else:
            game_list = Game.objects.filter(game_name__contains=txt)
    except Game.DoesNotExist:
        pass
    return render(request, 'index.html', {'games': game_list})

def add_game(request):
	if request.POST:
		gname = request.POST['GameName']
		gaddress = request.POST['GameAddress']
		gcompany = request.POST['GameCompany']
		game = Game(game_name = gname ,game_url = gaddress,game_company = gcompany)
		game.save()
	game_list = Game.objects.all()
	return render(request, "index.html", {'games': game_list})

def dele_game(request):
    try:
        id = request.GET['gid']
        Game.objects.filter(id=int(id)).delete()
        game_list = Game.objects.all()
    except Game.DoesNotExist:
        pass
    return render(request, 'index.html', {'games': game_list})

def selectUser(request):
    try:
        user_list = User.objects.all()
    except User.DoesNotExist:
        pass
    return render(request,'userinfo.html',{'users':user_list})

def addNews(request):
    links = AddNews()
    New = News.objects.all()
    if New:
        NewDB = New[0].pic_title
    else:
        NewDB = "";
    NewNet = links[0].find('h2').get_text()
    if NewNet.strip() == NewDB.strip():
        pass;
    else:
        New = News.objects.all()
        News.objects.all().delete()
        path = 'G:/GameApp/GameApp/static/sounds'
        for i in os.listdir(path):
            path_file = os.path.join(path, i)
            if os.path.isfile(path_file):
                os.remove(path_file)
        for link in links:
            title = link.find('h2').get_text()
            context = link.find('p').get_text().strip()
            picurl = link.find('img')['src']
            news = News(pic_url=picurl, pic_context=context, pic_title=title)
            news.save()
        for new in New:
            newsId = str(new.id)
            text = new.pic_context
            Read(text, newsId)
    return render(request, 'card.html',{'news':New})

# 获取天气信息
def getWeather(request):
    CityWeather = GetWeatherInfo()
    return render(request, 'weather.html', {'CityWeather': CityWeather})

def addArticle(request):
    if request.POST:
        aTitle = request.POST['Title']
        aAuthor = request.POST['Author']
        aContent = request.POST['Content']
        aTag = request.POST['Tag']
        aCreateTime = datetime.now()
        article = Article(arti_title=aTitle,arti_author=aAuthor,arti_content=aContent,arti_createtime=aCreateTime,arti_tag=aTag)
        article.save()
        return redirect("/article_list/")

def getArticles(request):
    userName = request.session['user_name']
    article_list = Article.objects.filter(arti_author=userName)
    return render(request,'article_list.html',{'article':article_list})

def showArticle(request):
    if request.GET:
        aNo = request.GET['art_no']
        article = Article.objects.filter(id = aNo)
        artTitle = article.values('arti_title').first()['arti_title']
        artContent = article.values('arti_content').first()['arti_content']
        return render(request,'article_show.html',{'article':[artTitle,artContent]})

# 发送邮件
def sendemail(request,email,user):
    # html_content = '<h2>你好，'+user+'：</h2><p>&nbsp; &nbsp; 欢迎您加入HC Pigg游戏联盟</p>'
    # msg = EmailMultiAlternatives('恭喜你注册成功！',
    #                              'huachongsz@163.com',
    #                              [email])
    # msg.attach_alternative(html_content, "text/html")
    #  msg.attach_file("")
    # msg.send()
    send_mail('恭喜你注册成功！',
              '你好，'+user+'：'
                     +'欢迎您加入HC Pigg游戏联盟',
              'huachongsz@163.com',
              [email],
              fail_silently=False)