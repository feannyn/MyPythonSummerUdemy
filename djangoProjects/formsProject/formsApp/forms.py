from django import forms

class formName(forms.FormModel):
	name = forms.CharField()
	email = forms.EmailField()
	text = forms.CharField(widget = forms.Textarea)

	#create hidden fields
	#the required attribute tells it to be a hidden field
	botcatcher = forms.CharField(required = False, widget = forms.HiddenInput)