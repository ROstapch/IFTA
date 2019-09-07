from django.urls import path, include

from . import views


app_name='Core'
urlpatterns = [
	path('companies/', views.companies, name='companies'),
	path('units/', views.all_units, name='all_units'),
	path('units/<int:unit_number>', views.unit_details, name='unit_details'),
]