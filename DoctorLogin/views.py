from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from .models import *
from django.contrib.auth import authenticate,logout,login
from django.utils import timezone

# Create your views here.

def homepage(request):
	return render(request,'index.html')


def loginpage(request):
	error = ""
	page = ""
	if request.method == 'POST':
		u = request.POST['email']
		p = request.POST['password']
		user = authenticate(request,username=u,password=p)
		try:
			if user is not None:
				login(request,user)
				error = "no"
				g = request.user.groups.all()[0].name
				if g == 'Doctor':
					page = "doctor"
					d = {'error': error,'page':page}
					return render(request,'doctorhome.html',d)
			else:
				error = "yes"
		except Exception as e:
			error = "yes"
			#print(e)
			#raise e
	return render(request,'login.html')