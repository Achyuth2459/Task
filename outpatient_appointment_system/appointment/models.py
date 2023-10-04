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
        ('4:00', '4:00'), ('4:15', '4:15'), ('4:30', '4:30'),('4:45', '4:45'),
        ('5:00', '5:00'),('5:15', '5:15'), ('5:30', '5:30'),('5:45', '5:45'),
        ('6:00', '6:00'),('6:15', '6:15'),('6:30', '6:30'),('6:45', '6:45'),
        ('7:00', '7:00'),('7:15', '7:15'),('7:30', '7:30'), ('7:45', '7:45'),
         
    ))
    
    def __str__(self):
        return f"Appointment with {self.doctor} on {self.appointment_date}"

