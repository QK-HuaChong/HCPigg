from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.core.mail import send_mail

def gameindex(request):
    return render(request,'index.html')

def login(request):
    return render(request,"login.html")

def page_not_found(request):
    return render_to_response('404.html')

def card(request):
    return render(request,'card.html')

def ui_card(request):
    return render(request, 'weather.html')

def article(request):
    return render(request,"article.html")

def article_list(request):
    return render(request,"article_list.html")

def sendemail(request):
    send_mail('测试邮件', '这是测试邮件', 'huachongsz@163.com', ['412777547@qq.com'], fail_silently=False)
    return  HttpResponse("<h3>发送成功</h3>")
