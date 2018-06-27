from django.urls import path, include
from . import views

urlpatterns = [
	path('help/', views.help, name='help'),
	path('users/', views.displayUsers, name='displayUsers'),
]
