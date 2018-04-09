from django.shortcuts import render,HttpResponse, redirect
from django import views
from app01 import models
from django.utils.decorators import method_decorator
# Create your views here.


def auth(func):
    def inner(request, *args, **kwargs):
        print(type(request.session))
        is_login = request.session['is_login']
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return redirect('login.html')
    return inner


class Login(views.View):

    def dispatch(self, request, *args, **kwargs):
        ret = super(Login, self).dispatch(request, *args, **kwargs)
        return ret

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {'message': ''})

    def post(self, request, *args, **kwargs):
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        c = models.Administrator.objects.filter(username=user, password=pwd).count()
        if c:
            request.session['user'] = user
            request.session['is_login'] = True
            rep = redirect('index.html')
            return rep
        else:
            message = "用户名或密码不正确"
            return render(request, 'login.html', {'message': message})







def auth(func):
    def inner(request, *args, **kwargs):
        print(type(request.session))
        is_login = request.session['is_login']
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return redirect('login.html')
    return inner


def login(request):
    message =''
    # models.Administrator.objects.create(
    #     username='root',
    #     password='123456'
    # )
    v = request.session
    print(type(v))
    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        c = models.Administrator.objects.filter(username=user, password=pwd).count()
        if c:
            request.session['is_login'] = True
            request.session['user'] = user
            rep = redirect('index.html')
            return rep
        else:
            message = "用户名账户密码错误!"
    obj = render(request, 'login.html', {'message': message})
    return obj


def logout(request):
    request.session.clear()
    return redirect('login.html')


@auth
def index(request):
    user = request.session['user']
    return render(request, 'index.html', {'user': user})


@auth
def handle_classes(request):
    user = request.session['user']
    class_list = models.Classes.objects.all()
    # models.Classes.objects.create(caption='一班')
    # models.Classes.objects.create(caption='二班')
    # models.Classes.objects.create(caption='三班')
    return render(request,
                  'classes.html',
                  {'user': user, 'class_list': class_list})


@auth
def handle_student(request):
    user = request.session['user']
    return render(request, 'student.html', {'user': user})


@auth
def handle_teacher(request):
    user = request.session['user']
    return render(request, 'teacher.html', {'user': user})



