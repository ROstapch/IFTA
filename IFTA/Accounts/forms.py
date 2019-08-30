from django import forms

class SigninForm(forms.Form):
	username = forms.CharField(label='Username', required=True, max_length=100)
	password = forms.CharField(label='Password', required=True, widget = forms.PasswordInput, max_length=50)
