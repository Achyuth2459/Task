import statistics
from django.conf import settings

from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('',welcome,name='welcome'),
    path('doctors/',doctorsList,name='doctorsList'),
    path('doctors/details/<int:id>/',doctorDetails, name='doctorDetails'),
    path('doctors/details/<int:id>/appointment/', appointment_form, name='appointment_form'),
    path('appointment/success/', appointment_success, name='appointment_success'),
    path('fail/', failed_booking, name='fail'),

]

