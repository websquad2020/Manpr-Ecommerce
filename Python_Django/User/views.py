from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import login, logout, authenticate
#from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UsersLoginForm, UsersRegisterForm


# Create your views here.
def login_view(request):
	form = UsersLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username = username, password = password)
		login(request, user)
		return redirect("home")
	return render(request, "form.html", {
		"form" : form,
		"title" : "Login",
	})

def register_view(request):
	form = UsersRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save()
		password = form.cleaned_data.get("password")	
		user.set_password(password)
		user.save()
		new_user = authenticate(username = user.username, password = password)
		login(request, new_user)
		return redirect("login")
	return render(request, "form.html", {
		"title" : "Register",
		"form" : form,
	})



