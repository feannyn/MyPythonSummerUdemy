from django.shortcuts import render

# Create your views here.
def base(request):
	return render(request, 'templatesApp/base.html')

def index(request):
	context_dict = {'text': 'hello world', 'number': 100}
	return render(request, 'templatesApp/index.html', context_dict)

def other(request):
	return render(request, 'templatesApp/other.html')

def relative_urls(request):
	return render(request, 'templatesApp/relative_urls.html')