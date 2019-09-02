from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse
from .API.api_requests import Company_Drivers, Company_Units
from .API.parse_response import ParseJSON
from .API.save_parsed_data import save_drivers

from .models import *



def companies(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("Accounts:signin"))
	if not request.user.has_perm('Core.view_company'):
		raise PermissionDenied()
	context = RequestContext(request)
	company_list = Company.objects.order_by('company_name')
	context_data = {'companies': company_list}
	'''
	if Company.objects.all():
		company = Company.objects.filter(company_name="Precise Transportation")
		if company:
			temp = Company_Drivers.Get_All_Drivers(comp = company)
			resp = temp.send_request()
			if resp:
				if resp.status_code == 200:
					user_list = ParseJSON.users(resp.text)
					for user in user_list:
						print(user)
					save_drivers(user_list)
				else:
					print(resp.status_code)
			else:
				print("Errors with request")
		else:
			print("No company with such name")
	else:
		print("No companies available")
	'''
	if Company.objects.all():
		company = Company.objects.filter(company_name="Precise Transportation")
		if company:
			#temp = Company_Units.Get_Unit_Id(units_id = 64801, comp = company)
			temp = Company_Units.Get_All_Units(comp = company)
			resp = temp.send_request()
			if resp:
				if resp.status_code == 200:
					unit_list = ParseJSON.units(resp.text)
					for unit in unit_list:
						print(unit)
				else:
					print(resp.status_code)
			else:
				print("Errors with request")
		else:
			print("No company with such name")
	else:
		print("No companies available")
	

	return render_to_response('Core/companies.html', context_data, context)
