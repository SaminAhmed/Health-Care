from django.db import models

class Appointment(models.Model):
	doctorname = models.CharField(max_length=50)
	doctoremail = models.EmailField(max_length=50)
	patientname = models.CharField(max_length=50)
	patientemail = models.EmailField(max_length=50)
	appointmentdate = models.DateField(max_length=10)
	appointmenttime = models.TimeField(max_length=10)
	symptoms = models.CharField(max_length=100)
	status = models.BooleanField()
	prescription = models.CharField(max_length=200)
	
	def __str__(self):
		return self.patientname+" you have appointment with "+self.doctorname