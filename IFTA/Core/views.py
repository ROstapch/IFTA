from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def homepage(request):
	return render(request, 'Core/homepage.html')