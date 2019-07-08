from django.shortcuts import render

# Create your views here.
from userapp.models import TUser


def login(request):
    return render(request,'userapp/login.html')

def login_ok(request):
    username = request.POST.get('userid')
    password = request.POST.get('psw')
    result = TUser.objects.filter(username=username,password=password)
    if result:
        return render(request,'main.html')
    else:
        return render(request,'userapp/login.html')


def regist(request):
    return render(request, 'userapp/registe.html')


def regist_ok(request):
    username = request.POST.get('userid')
    phone = request.POST.get('usrtel')
    email = request.POST.get('email')
    password = request.POST.get('psw')
    u1 = TUser.objects.create(username=username,phone=phone,email=email,password=password)
    return render(request,'userapp/login.html')

