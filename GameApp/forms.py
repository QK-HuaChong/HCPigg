from django import forms
from captcha.fields import CaptchaField

class UserFrom(forms.Form):
    username = forms.CharField(label="账户",max_length=35,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'用户名'}))
    password = forms.CharField(label="密码",max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'密码'}))
    captcha = CaptchaField(label='验证码')

class RegisterForm(forms.Form):
    gender = (
        ('male','-男-'),
        ('female','-女-'),
    )
    username = forms.CharField(label="用户名",max_length=128,widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="密码", max_length=255,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=255,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱",widget=forms.EmailInput(attrs={'class':'form-control'}))
    sex = forms.ChoiceField(label="性别",choices=gender)

class ArticleForm(forms.Form):
    articletitle = forms.CharField(max_length=255)
    articleauthor = forms.CharField(max_length=125)
    articlecontent = forms.CharField(widget=forms.Textarea)
    artilecreatetime = forms.TimeField()
