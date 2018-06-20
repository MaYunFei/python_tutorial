from django.shortcuts import render, redirect

# Create your views here.
from login import models, forms


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "所有字段都必须填写！"
        if login_form.is_valid():  # 确保用户名和密码都不为空
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/login/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())
    login_form = forms.UserForm()  # 条件不成立也需要添加一个 form
    return render(request, 'login/login.html', locals())


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect("/index/")
