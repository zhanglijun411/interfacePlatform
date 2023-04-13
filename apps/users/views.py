from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import redirect, reverse
from apps.users.models import Users

# Create your views here.

def loginView(request):
    Login = True
    title = '用户登录'
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if Users.objects.filter(username=username):
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                return redirect(reverse('interface:homePage'), locals())
            else:
                tips = '密码错误'
        else:
            tips = '用户不存在'
    return render(request, 'users/user.html', locals())


def registerView(request):
    Login = False
    title = '用户注册'

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        real_name = request.POST.get('real_name', '')
        email = request.POST.get('email', '')

        if username == '':
            tips = '用户名不能为空'
        elif password == '':
            tips = '密码不能为空'
        elif real_name == '':
            tips = '真实姓名不能为空'
        elif email == '':
            tips = '邮箱不能为空'
        else:

            if len(password) < 6:
                tips = '密码不能小于6位'
            elif password != password2:
                tips = '密码不一致'
            elif checkUsername(username):
                tips = '用户名只能输入英文'
            else:
                userInfo = {
                    'username': username,
                    'password': password,
                    'real_name': real_name,
                    'email': email
                }
                print('userInfo是：', userInfo)
                user = Users.objects.create_user(**userInfo)
                return redirect(reverse('users:login'), locals())

            return render(request, 'users/user.html', locals())

    return render(request, 'users/user.html', locals())

def logoutView(request):
    logout(request)

def checkUsername(username):
    specific_str = '!@#$%^&*()_+=-`~/,.;[]\\{}|:"<>?'
    for i in specific_str:
        if i in username:
            return True

    for cha in username:
        if not ('a' <= cha <= 'z' or 'A' <= cha <= 'Z'):
            return True
    return False
