from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from .models import *
from django.contrib.auth import authenticate,logout,login
from django.utils import timezone



# Create your views here.


def adminaddDoctor(request):
	error = ""
	user="none"
	if not request.user.is_staff:
		return redirect('login_admin')

	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		password = request.POST['password']
		repeatpassword =  request.POST['repeatpasssword']
		gender = request.POST['gender']
		phonenumber = request.POST['phonenumber']
		address = request.POST['address']
		birthdate = request.POST['dateofbirth']
		bloodgroup = request.POST['bloodgroup']
		specialization = request.POST['specialization']
		
		try:
			if password == repeatpassword:
				Doctor.objects.create(name=name,email=email,password=password,gender=gender,phonenumber=phonenumber,address=address,birthdate=birthdate,bloodgroup=bloodgroup,specialization=specialization)
				user = User.objects.create_user(first_name=name,email=email,password=password,username=email)
				doc_group = Group.objects.get(name='Doctor')
				doc_group.user_set.add(user)
				user.save()
				error = "no"
			else:
				error = "yes"
		except Exception as e:
			error = "yes"
	f = {'error' : error}
	return render(request,'adminadddoctor.html',f)
	
def AdminHome(request):
	
	if not request.user.is_staff:
		return redirect('login_admin')
	return render(request,'adminhome.html')
