import queue
from django import forms
from .models import Appointment
from django.db.models import Q

from datetime import datetime, timedelta



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient_name', 'appointment_date', 'appointment_time']

   
        