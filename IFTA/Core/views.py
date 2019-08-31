from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse
from .API.api_requests import Company_Drivers

from .models import *



def companies(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("Accounts:signin"))
	if not request.user.has_perm('Core.view_company'):
		raise PermissionDenied()
	context = RequestContext(request)
	company_list = Company.objects.order_by('company_name')
	context_data = {'companies': company_list}

	#temp = Company_Drivers.Get_All_Drivers(comp = Company.objects.select_related().filter(company_name="Precise Transportation"))
	#resp = temp.send_request()


	return render_to_response('Core/companies.html', context_data, context)
