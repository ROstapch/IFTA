from django.urls import path

from . import views


app_name='Core'
urlpatterns = [
	path('', views.Homepage, name = 'home'),
    path('companies/', views.Companies, name='companies'),
]