from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from .models import *
from django.contrib.auth import authenticate,logout,login
from django.utils import timezone

def Home(request):
	if not request.user.is_active:
		return redirect('loginpage')

	g = request.user.groups.all()[0].name
	if g == 'Doctor':
		return render(request,'doctorhome.html')
	

def profile(request):
	if not request.user.is_active:
		return redirect('loginpage')

	g = request.user.groups.all()[0].name
	
	if g == 'Doctor':
		doctor_detials = Doctor.objects.all().filter(email=request.user)
		d = { 'doctor_detials' : doctor_detials }
		return render(request,'doctorprofile.html',d)
	

	