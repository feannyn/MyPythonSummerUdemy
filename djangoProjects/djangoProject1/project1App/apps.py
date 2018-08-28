from django.apps import AppConfig
from django.http import HttpResponse

class Project1AppConfig(AppConfig):
    name = 'project1App'

def index(request):
	return HttpResponse("Hello World!")
