from django.urls import path

from . import views

app_name = 'Convert'
urlpatterns = [
	path('csv', views.upload_csv, name = 'upload_csv'),
]