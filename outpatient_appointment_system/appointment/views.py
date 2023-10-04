import queue
from django.forms import ValidationError
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *
from .forms import AppointmentForm
from django.shortcuts import render,redirect
from django.db.models import Q



def welcome(request):
    template= loader.get_template('main.html')
    return HttpResponse(template.render())
def doctorsList(request):
    doctors_list = Doctor.objects.all()
    template= loader.get_template('doctors_list.html')
    return HttpResponse(template.render({'doctors_list': doctors_list},request))
def doctorDetails(request,id):
    doctor_details = Doctor.objects.get(id=id)
    template= loader.get_template('doctor_detail.html')
    return HttpResponse(template.render({'doctor_details': doctor_details},request))

def appointment_form(request,id):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            doc=form.cleaned_data['doctor']
            time=form.cleaned_data['appointment_time']
            date=form.cleaned_data['appointment_date']
            day_of_week = date.strftime('%A')
            data= Appointment.objects.filter(Q(appointment_time=time)
                                              & Q(appointment_date=date) & Q(doctor__name=doc.name))
            appointment_count = Appointment.objects.filter(Q(appointment_date=date) & Q(doctor__name=doc.name)).count()
            
    
            if appointment_count >= doc.max_patients :
               template= loader.get_template('limit.html')
               return HttpResponse(template.render())

            if data or day_of_week == "Sunday" :
              return redirect('fail')
            
            form.save()
            template= loader.get_template('success.html')
            # return redirect('appointment_success')
            return HttpResponse(template.render())
    else:
        form = AppointmentForm()
    
    return render(request, 'bookappointment.html', {'form': form})
def failed_booking(request):
      template=loader.get_template('fail.html')
      return HttpResponse(template.render())

def limit_exceeded():
    template=loader.get_template('limit.html')
    return HttpResponse(template.render())

def appointment_success(request):
    return render(request, 'success.html')