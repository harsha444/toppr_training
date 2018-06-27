from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import NewUserForm

def index(request):
	return render(request, 'index.html')

def help(request):
	question = {'help': 'This is a help Page'}
	return render(request, 'help.html', question)

def displayUsers(request):
	form = NewUserForm()

	if request.method == "POST":
		form = NewUserForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print("ERROR FORM INVALID")
	return render(request, 'user.html', {'form':form})
