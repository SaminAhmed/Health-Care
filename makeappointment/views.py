from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from .models import *
#from django.contrib.auth import authenticate,logout,login
from django.utils import timezone
# Create your views here.


def MakeAppointments(request):
	error = ""
	if not request.user.is_active:
		return redirect('loginpage')
	alldoctors = Doctor.objects.all()
	doct = { 'alldoctors' : alldoctors }
	group = request.user.groups.all()[0].name
	if group == 'Patient':
		if request.method == 'POST':
			doctoremail = request.POST['doctoremail']
			doctorname = request.POST['doctorname']
			patientname = request.POST['patientname']
			patientemail = request.POST['patientemail']
			appointmentdate = request.POST['appointmentdate']
			appointmenttime = request.POST['appointmenttime']
			symptoms = request.POST['symptoms']
			try:
				Appointment.objects.create(doctorname=doctorname,doctoremail=doctoremail,patientname=patientname,patientemail=patientemail,appointmentdate=appointmentdate,appointmenttime=appointmenttime,symptoms=symptoms,status=True,prescription="")
				error = "no"
			except:
				error = "yes"
			errors = {"error":error}
			return render(request,'pateintmakeappointments.html',errors)
		elif request.method == 'GET':
			return render(request,'pateintmakeappointments.html',doct)
