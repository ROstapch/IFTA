from django.urls import path

from . import views

app_name = 'Accounts'
urlpatterns = [
	path('home/', views.homepage_view, name = 'home'),
	path('', views.homepage_view, name = 'home'),
	path('account/', views.account_view, name = 'account'),
	path('account/signin/', views.signin_view, name = 'signin'),
	path('account/signup/', views.signup_view, name = 'signup'),
	path('account/signout/', views.signout_view, name = 'signout'),
]