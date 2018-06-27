from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def index(request):
	return HttpResponse("<em>This is fun</em>")

def help(request):
	question = {'help': 'This is a help Page'}
	return render(request, 'help.html', question)

def displayUsers(request):
	user_list = User.objects.order_by('first_name')
	users = {'users':user_list}
	return render(request, 'user.html', users)
