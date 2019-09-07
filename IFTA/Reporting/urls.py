from django.urls import path

from . import views


app_name='Reporting'
urlpatterns = [
	path('', views.reports, name='reports')
]
