from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from .models import *
from django.contrib.auth import authenticate,logout,login
from django.utils import timezone

# Create your views here.

def homepage(request):
	return render(request,'index.html')


def Login_admin(request):
	error = ""
	if request.method == 'POST':
		u = request.POST['username']
		p = request.POST['password']
		user = authenticate(username=u,password=p)
		try:
			if user.is_staff:
				login(request,user)
				error = "no"
			else:
				error = "yes"
		except:
			error = "yes"
	d = {'error' : error}
	return render(request,'adminlogin.html',d)
def AdminHome(request):
	if not request.user.is_staff:
		return redirect('login_admin')
	return render(request,'adminhome.html')

def Logout_admin(request):
	if not request.user.is_staff:
		return redirect('login_admin')
	logout(request)
	return redirect('login_admin')

