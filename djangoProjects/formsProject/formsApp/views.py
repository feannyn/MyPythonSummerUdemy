from django.shortcuts import render
from formsApp import forms

# Create your views here.
def index(request):
	return render(request, 'formsApp/index.html')

def form_name_view(request):
	form = forms.formName()

	if request.method == "POST":
		form = forms.formName(request.POST)

		if form.is_valid():
			#DO SOMETHING WITH DATA HERE
			print("Validation success!!!!!")
			print("NAME: " + form.cleaned_data['name'])
			print("EMAIL: " + form.cleaned_data['email'])
			print("TEXT: " + form.cleaned_data['text'])

			


	return render(request,'formsApp/form.html', {'form': form})