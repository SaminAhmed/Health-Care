from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from .models import *
from django.contrib.auth import authenticate,logout,login
from django.utils import timezone


# Create your views here.

def Home(request):
	if not request.user.is_active:
		return redirect('loginpage')

	group = request.user.groups.all()[0].name
	if group == 'Patient':
		return render(request,'patienthome.html')

def profile(request):
	if not request.user.is_active:
		return redirect('loginpage')

	group = request.user.groups.all()[0].name
	if group == 'Patient':
		patient_detials = Patient.objects.all().filter(email=request.user)
		details = { 'patient_detials' : patient_detials }
		return render(request,'pateintprofile.html',details)


