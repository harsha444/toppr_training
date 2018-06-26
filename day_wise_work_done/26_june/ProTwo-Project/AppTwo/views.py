from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("<em>This is fun</em>")

def help(request):
	question = {'help': 'This is a help Page'}
	return render(request, 'help.html', question)