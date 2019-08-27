from django.urls import path, include

from . import views


app_name='Core'
urlpatterns = [
	path('', views.homepage, name = 'home'),
	path('companies/', views.companies, name='companies')
]