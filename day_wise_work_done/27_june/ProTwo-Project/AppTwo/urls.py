from django.urls import path, include
from . import views
from . import forms

urlpatterns = [
	path('', views.index, name='index'),
	path('help/', views.help, name='help'),
	path('users/', views.displayUsers, name='displayUsers'),
]
