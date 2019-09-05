from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from Accounts.forms import SigninForm
from django.http import Http404



def homepage_view(request):
	return render(request, 'Accounts/homepage.html')



def account_view(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("Accounts:signin"))
	return render(request, 'Accounts/account.html')



def signup_view(request):
	return render(request, 'Accounts/signup.html')



def signin_view(request):
	if 'POST' == request.method:
		form = SigninForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = authenticate(request, username=data['username'], password=data['password'])
			if user is not None:
				login(request, user)
				return HttpResponseRedirect(reverse("Accounts:account"))
		return render(request, 'Accounts/signin.html', context={'error_message':"Incorrect username or password", 'form' : SigninForm()})
	else:
		form = SigninForm()
		return render(request, 'Accounts/signin.html', {'form' : form})



def signout_view(request):
	if not request.user.is_authenticated:
		raise Http404("You can't be signed out, because you are not signed in")
	else:
		logout(request)
		return HttpResponseRedirect(reverse("Accounts:home"))
