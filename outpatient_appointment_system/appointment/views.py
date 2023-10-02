from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *
  

def doctorsList(request):
    doctors = Doctor.objects.all()
    