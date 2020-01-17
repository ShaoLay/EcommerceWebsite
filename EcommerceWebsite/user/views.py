from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.

from user.forms import UserForm
from user.models import User

def register(request):
    if request.method == 'POST':  # 判断表单是否提交状态
        uf = UserForm(request.POST)  # 判断表单变量
        if uf.is_valid():  # 判断表单数据是否正确
            # 获取表单
            username = (request.POST.get('username')).strip()
            password = (request.POST.get('password')).strip()
            email = request.POST.get('email')


            # 查找数据库中存在相同的用户名
            user_list = User.objects.filter(username=username)
            if user_list:
                # 如果存在,就报'用户名已经存在！', 并且回到注册页面
                return render_to_response('register.html', {'uf': uf, "error": "用户名已经存在！"})
            else:
                # 否则将表单写入数据库
                user = User()
                user.username = username
                user.password = password
                user.email = email
                user.save()
                # 返回登录页面
                # uf = LoginForm()
                return render_to_response('login.html', {'uf': uf})
    else:  # 如果不是表单提交状态, 就显示表单信息
        uf = UserForm()
    return render_to_response('register.html', {'uf': uf})
