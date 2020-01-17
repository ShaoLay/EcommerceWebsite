from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from login.forms import LoginForm
from user.models import User

def login(request):
    return render_to_response('login.html')

def login_action(request):
    if request.method == 'POST':
        uf = LoginForm(request.POST)
        if uf.is_valid():
            username = (request.POST.get('username')).strip()
            password = (request.POST.get('password')).strip()
            if username == '' or password == '':
                return render(request, 'login.html', {'uf':uf, "error":'用户名或密码不能为空！'})
            else:
                user = User.objects.filter(username=username, password=password)
                if user:
                    response = HttpResponseRedirect('/index/')
                    request.session['username'] = username
                    return response
                else:
                    return render(request, 'login.html', {'uf':uf, "error":'用户名或密码错误'})
        else:
            uf = LoginForm()
        return render_to_response('login.html', {'uf':uf})