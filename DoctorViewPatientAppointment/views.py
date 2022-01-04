from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from .models import *
from django.contrib.auth import authenticate,logout,login
from django.utils import timezone

def viewappointments(request):
	if not request.user.is_active:
		return redirect('loginpage')
	
	group = request.user.groups.all()[0].name
	
	if group == 'Doctor':
		if request.method == 'POST':
			prescriptiondata = request.POST['prescription']
			idvalue = request.POST['idofappointment']
			Appointment.objects.filter(id=idvalue).update(prescription=prescriptiondata,status=False)
			
		upcomming_appointments = Appointment.objects.filter(doctoremail=request.user,appointmentdate__gte=timezone.now(),status=True).order_by('appointmentdate')
		
		previous_appointments = Appointment.objects.filter(doctoremail=request.user,appointmentdate__lt=timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(doctoremail=requsest.user,status=False).order_by('-appointmentdate')
		
		data = { "upcomming_appointments" : upcomming_appointments, "previous_appointments" : previous_appointments }
		return render(request,'doctorviewappointment.html',data)
