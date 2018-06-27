from django.urls import path, include
from . import views

# Template tagging
app_name = 'basic_app'

urlpatterns = [
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative')
]
