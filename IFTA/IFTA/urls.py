from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('Core.urls')),
	path('convert/', include('Convert.urls')),
    path('admin/', admin.site.urls),
]
