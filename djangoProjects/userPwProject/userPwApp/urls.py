from django.urls import path
from django.urls import re_path
from django.urls import include
from userPwApp import views


#TEMPLATE URLS
app_name = 'userPwApp'

urlpatterns = [
	re_path(r'^registration/$', views.registration, name = 'registration'),
	re_path(r'^user_login/$', views.user_login, name = 'user_login'),
]