from django.urls import path

from mainapp import views

app_name = 'mainapp'
urlpatterns = [
    path('login/',views.main,name='main'),

]