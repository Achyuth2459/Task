import datetime
from django.db import models

class Doctor(models.Model):
   name= models.CharField(max_length=50)
   specialty = models.CharField(max_length=100)
   max_patients = models.PositiveIntegerField(default=10)

   def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    appointment_date = models.DateField(default=datetime.datetime.now().date)
    appointment_time = models.CharField(max_length=20, choices=(
        ('select', 'select'),
        ('4:00', '4:00'),
        ('5:00', '5:00'),
        ('6:00', '6:00'),
        ('7:00', '7:00'),
        ('8:00', '8:00'),
        ('9:00', '9:00'),
    ))
    
    def __str__(self):
        return f"Appointment with {self.doctor} on {self.appointment_date}"

