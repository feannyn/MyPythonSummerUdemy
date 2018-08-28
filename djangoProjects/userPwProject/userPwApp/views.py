from django.shortcuts import render
from userPwApp.forms import UserProfileInfoForm, UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
	return render(request, 'userPwApp/index.html')


@login_required #this is a decorated for the user_logout function
def user_logout(request):
	logout(request)
	return HttpResponse(reverse('index'))


def registration(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileInfoForm(data = request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save() #will save user data to DB 
			user.set_password(user.password)#sets pw as hash
			user.save() #save the hashed value to the DB 

			profile = profile_form.save(commit = false)
			profile.user = user

			if 'profile_pic' in request.FILES: #'reuqest.FILES takes in the docs that the user gives to be stored'
				profile.profile_pic = request.FILES['profile_pic']#dictionary of all files sent in by user in "POST"

			profile.save()
			registered = True

		else:
			print(user_form.errors, profile_forms.errors)
	else:
			user_form = UserForm()
			profile_form = UserProfileInfoForm()

	return render(request, 'userPwApp/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		#auto authenticates the user 
		user = authenticate(username = username, password = password)

		if user:
			if user.is_active():
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("ACCOUNT NOT ACTIVE")
		else:
			print("someone attempted to login and failed...")
			print("Username: {} and password: {}".format(username, password))
			return HttpResponse("Invalid login details supplied")
	else:
		return render(request, 'userPwApp/login.html', {})






