from django.db import models

class Game(models.Model):
    game_name = models.CharField(max_length=20)
    game_url = models.CharField(max_length=32)
    game_company = models.CharField(max_length=50)

class User(models.Model):
    user_name = models.CharField(max_length=125)
    user_pwd = models.CharField(max_length=135)
    user_email = models.CharField(max_length=120)
    user_sex = models.CharField(max_length=5)

class News(models.Model):
    pic_title = models.CharField(max_length=125)
    pic_context = models.CharField(max_length=255)
    pic_url = models.CharField(max_length=125)

class Article(models.Model):
    arti_title = models.CharField(max_length=125)
    arti_author = models.CharField(max_length=50)
    arti_tag = models.CharField(max_length=20)
    arti_content = models.TextField()
    arti_createtime = models.DateTimeField(auto_now_add=True)

