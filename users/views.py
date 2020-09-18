from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import List
from .forms import List_form

from .forms import SignUpForm

def signup_view(request):
	if request.user.is_authenticated:
		return redirect('users:dashboard')
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('users:dashboard')
		else:
			messages.error(request, 'Correct the errors below')
	else:
		form = SignUpForm()

	return render(request, 'app/signup.html', {'form': form})



def home_view(request):
	return render(request, 'app/home.html')

@login_required
def dashboard_view(request):
    form = List_form()
    if request.method == "POST":
        form = List_form(request.POST)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'app/dashboard.html', context)


def task_list(request):
    s = List.objects.all()
    print(s)
    context = {'s': s}
    return render(request, 'app/tasktable.html', context)

def data(request):
    s = List.objects.all()
    print(s)
    context = {'s': s}
    return render(request, 'app/delete.html', context)



def new_task(request):
    s = List.objects.all()
    print(s)
    context = {'s': s}
    return render(request, 'ok.html', context)

def  deleteTask(request,pk):
    task = List.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
    context={'item':task}
    return render(request,'app/delete_task.html',context)

