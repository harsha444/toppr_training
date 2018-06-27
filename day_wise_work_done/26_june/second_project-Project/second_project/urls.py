from django.contrib import admin
from django.urls import path, include
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('first_app/', include('first_app.urls'))
]
