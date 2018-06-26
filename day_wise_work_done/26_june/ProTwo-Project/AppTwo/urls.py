from django.urls import path, include
from . import views

urlpatterns = [
	path('help/', views.help, name='help'),
]