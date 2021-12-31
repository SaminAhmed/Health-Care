from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from .models import *
from django.contrib.auth import authenticate,logout,login
from django.utils import timezone


def viewappointments(request):
	if not request.user.is_active:
		return redirect('loginpage')
	#print(request.user)
	g = request.user.groups.all()[0].name
	if g == 'Patient':
		upcomming_appointments = Appointment.objects.filter(patientemail=request.user,appointmentdate__gte=timezone.now(),status=True).order_by('appointmentdate')
		#print("Upcomming Appointment",upcomming_appointments)
		previous_appointments = Appointment.objects.filter(patientemail=request.user,appointmentdate__lt=timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(patientemail=request.user,status=False).order_by('-appointmentdate')
		#print("Previous Appointment",previous_appointments)
		d = { "upcomming_appointments" : upcomming_appointments, "previous_appointments" : previous_appointments }
		return render(request,'patientviewappointments.html',d)
	
