from django.urls import path

from . import views

app_name = 'Convert'
urlpatterns = [
	path('csv/upload', views.upload_csv, name = 'upload_csv'),
]