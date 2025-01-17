from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('Accounts.urls')),
	path('general/', include('Core.urls')),
	path('convert/', include('Convert.urls')),
	path('reports/', include('Reporting.urls')),
	path('admin/', admin.site.urls)
]
