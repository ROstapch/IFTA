from django.urls import path

from . import views

app_name = 'Accounts'
urlpatterns = [
	path('home/', views.homepage_view, name = 'home'),
	path('', views.homepage_view, name = 'home'),
	path('account/', views.account_view, name = 'account'),
	path('account/register/', views.register_view, name = 'registration'),
	path('account/login/', views.login_view, name = 'login'),
	path('account/logout/', views.logout_view, name = 'logout'),
]