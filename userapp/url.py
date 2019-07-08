from django.urls import path

from userapp import views

app_name = 'userapp'
urlpatterns = [
    path('login/',views.login,name='login'),
    path('login_ok/',views.login_ok,name='login_ok'),
    path('regist/',views.regist,name='regist'),
    path('regist_ok/',views.regist_ok,name='regist_ok'),
]
