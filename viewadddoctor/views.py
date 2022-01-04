from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from .models import *
from django.contrib.auth import authenticate,logout,login
from django.utils import timezone



def adminviewDoctor(request):
	if not request.user.is_staff:
		return redirect('login_admin')
	doc = Doctor.objects.all()
	f = { 'doc' : doc }
	return render(request,'adminviewDoctors.html',f)
	
def admin_delete_doctor(request,pid,email):
	if not request.user.is_staff:
		return redirect('login_admin')
	doctor = Doctor.objects.get(id=pid)
	doctor.delete()
	users = User.objects.filter(username=email)
	users.delete()
	return redirect('adminviewDoctor')

def AdminHome(request):
	
	if not request.user.is_staff:
		return redirect('login_admin')
	return render(request,'adminhome.html')


