from django import forms
from djangoChallenge1App.models import User

class MyForm(forms.ModelForm):
	#validator bot catcher 
	botcatcher = forms.CharField(required = False, widget = forms.HiddenInput)

	#use MetaClass
	class Meta:
		model = User
		fields = "__all__"
