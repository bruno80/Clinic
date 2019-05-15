from django.urls import path
from . import views

urlpatterns = [
  path('', views.home),
  path('doctor/',views.doctor_show),
  path('patient/',views.patient_show)
]
