from django.shortcuts import render
from django.http import HttpResponse
#from djangoChallenge1App.models import User
from django.shortcuts import render
from djangoChallenge1App.forms import MyForm

# Create your views here.
def index(request):
	ind_dict = {'test': "<h2>IT WAS SUCESSFUL YAYAYAYAYAYYAAYYAYAY</h2>"}
	return render(request,"djangoChallenge1App/index.html", context=ind_dict)

def help(request):
	help_dict = {'help':"This is the help page"}
	return render(request,"djangoChallenge1App/help.html", context=help_dict)

def user(request):
	#create a User template
	#email list will make a list of objects within User and order them by date
	email_list = User.objects.order_by('l_name')

	#email_dict is what will be pushed to the html page
	email_dict = {'email': email_list}

	#return the render function 
	return render(request,'djangoChallenge1App/user.html', context = email_dict)

def form_view(request):
	#create instance of the form class you want to use 
	form = MyForm()


	if request.method == "POST":
		#if request is a POST; set form to new object with
		#the request passed in
		form = MyForm(request.POST)

		if form.is_valid():
			#DO SOMETHING WITH DATA HERE
			print("Validation success!!!!!")
			print("FIRST NAME: " + form.cleaned_data['f_name'])
			print("LAST NAME: " + form.cleaned_data['l_name'])
			print("EMAIL: " + form.cleaned_data['email'])

			user = form.save(commit = False)
			user.f_name = form.cleaned_data['f_name']
			user.l_name = form.cleaned_data['l_name']
			user.email = form.cleaned_data['email']
			user.save()

	#{'form':form} is a dictionary which the key is form and we pass as the value the form object 
	#we created above
	return render(request,'djangoChallenge1App/signup.html', {'form':form} )
