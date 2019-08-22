from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('convert/', include('Convert.urls')),
    path('admin/', admin.site.urls),
]
