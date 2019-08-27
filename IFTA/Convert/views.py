from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .processing.convertion import EFS_to_KT_convert as convert_file
from django.contrib.auth.decorators import login_required

def upload_csv(request):
	if "GET" == request.method:
		return render(request, "Convert/convert.html")

	elif "POST" == request.method:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			return HttpResponseRedirect(reverse("Convert:upload_csv"))

		else:
			return convert_file(csv_file)
