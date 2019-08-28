from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label='username', required=True, max_length=100)
	password = forms.CharField(label='password', required=True, widget = forms.PasswordInput, max_length=50)
