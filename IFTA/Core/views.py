from django.shortcuts import render, render_to_response
from django.views import generic
from django.template import RequestContext
from .models import *


def Homepage(request):
	return render(request, 'Core/homepage.html')

def Companies(request):
	context = RequestContext(request)
	company_list = Company.objects.order_by('company_name')
	context_data = {'companies': company_list}
	return render_to_response('Core/companies.html', context_data, context)
