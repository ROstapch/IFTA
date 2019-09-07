from django.shortcuts import render
from django.template import RequestContext
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from Core.API.KeepTruckinAPI import *

from .models import *



def all_units(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("Accounts:signin"))
	context = RequestContext(request)
	units_list = Unit.objects.order_by('unit_number')
	context_data = {'units': units_list}
	return render(request, 'Core/all_units.html', context_data, request)


def unit_details(request, unit_number):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("Accounts:signin"))
	context = RequestContext(request)
	unit = Unit.objects.get(unit_number = unit_number)
	context_data = {'unit': unit}
	return render(request, 'Core/unit.html', context_data, request)



def companies(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("Accounts:signin"))
	if not request.user.has_perm('Core.view_company'):
		raise PermissionDenied()
	context = RequestContext(request)
	company_list = Company.objects.order_by('company_name')
	context_data = {'companies': company_list}
	return render(request, 'Core/companies.html', context_data, request)
