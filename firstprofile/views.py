from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from .models import *
from django.contrib.auth import authenticate,logout,login
from django.utils import timezone


# Create your views here.
def homepage(request):
	return render(request,'index.html')

def createaccountpage(request):
	error = ""
	user="none"
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		password = request.POST['password']
		repeatpassword = request.POST['repeatpassword']
		gender = request.POST['gender']
		phonenumber = request.POST['phonenumber']
		address = request.POST['address']
		birthdate = request.POST['dateofbirth']
		bloodgroup = request.POST['bloodgroup']
		try:
			if password == repeatpassword:
				Patient.objects.create(name=name,email=email,password=password,gender=gender,phonenumber=phonenumber,address=address,birthdate=birthdate,bloodgroup=bloodgroup)
				user = User.objects.create_user(first_name=name,email=email,password=password,username=email)
				pat_group = Group.objects.get(name='Patient')
				pat_group.user_set.add(user)
				#print(pat_group)
				user.save()
				#print(user)
				error = "no"
			else:
				error = "yes"
		except Exception as e:
			error = "yes"
			#print("Error:",e)
	d = {'error' : error}
	#print(error)
	return render(request,'createaccount.html',d)
	

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
				if g == 'Patient':
					page = "patient"
					d = {'error': error,'page':page}
					return render(request,'patienthome.html',d)
			else:
				error = "yes"
		except Exception as e:
			error = "yes"
			#print(e)
			#raise e
	return render(request,'login.html')



def Home(request):
	if not request.user.is_active:
		return redirect('loginpage')

	g = request.user.groups.all()[0].name
	if g == 'Patient':
		return render(request,'patienthome.html')

def profile(request):
	if not request.user.is_active:
		return redirect('loginpage')

	g = request.user.groups.all()[0].name
	if g == 'Patient':
		patient_detials = Patient.objects.all().filter(email=request.user)
		d = { 'patient_detials' : patient_detials }
		return render(request,'pateintprofile.html',d)
	

