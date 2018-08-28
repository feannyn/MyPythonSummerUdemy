from django.urls import re_path, path
from djangoChallenge1App import views

urlpatterns = [
	re_path(r'^$', views.user, name = "user"),		
]