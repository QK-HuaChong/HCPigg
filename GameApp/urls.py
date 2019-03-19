"""GameApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views,games

urlpatterns = [
    path('login/',games.login),
    path('logout/', games.logout),
    path('register/',games.regiter),
    path('index/', games.selectAll),
    path('gameList/',games.selectAll),
    path('search/',games.search_game),
    path('addGame/',games.add_game),
    path('article/',views.article),
    path('add_article/',games.addArticle),
    path('article_list/',games.getArticles),
    path('show_article/',games.showArticle),
    path('news/',games.addNews),
    path('dele/',games.dele_game),
    path('weather/',games.getWeather),
    path('captcha', include('captcha.urls')),

#     USER INFO
    path('user/',games.selectUser)
]
