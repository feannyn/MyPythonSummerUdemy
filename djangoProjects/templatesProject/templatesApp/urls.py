from django.urls import path
from django.urls import re_path
from templatesApp import views

#FOR TEMPLATE TAGGING
#create app name and set it to the name of the app
app_name = 'templatesApp'

urlpatterns = [
	re_path(r'^other/$', views.other, name = 'other'),
	re_path(r'^relative_urls/$', views.relative_urls, name = 'relative_urls'),
]