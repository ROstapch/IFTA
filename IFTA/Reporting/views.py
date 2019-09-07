from django.shortcuts import render

def reports(request):
	return render(request, "Reporting/reports.html")