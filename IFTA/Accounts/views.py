from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def homepage_view(request):
	return render(request, 'Accounts/homepage.html')



def account_view(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("Accounts:login"))
	return render(request, 'Accounts/account.html')



def register_view(request):
	return render(request, 'Accounts/register.html')



def login_view(request):
	if 'POST' == request.method:
		form = LoginForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = authenticate(request, username=data['username'], password=data['password'])
			if user is not None:
				login(request, user)
				return HttpResponseRedirect(reverse("Accounts:account"))
		return render(request, 'Accounts/login.html', context={'error_message':"Incorrect username or password", 'form' : LoginForm()})
	else:
		form = LoginForm()
		return render(request, 'Accounts/login.html', {'form' : form})



def logout_view(request):
	return render(request, 'Accounts/logout.html')
