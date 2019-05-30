from django.urls import path
from . import views

urlpatterns = [
  path('', views.home),
  path('doctor/',views.doctor_list),
  path('patient/',views.patient_list),
  path('doctor/new/',views.doctor_new),
  path('patient/new/',views.patient_new),
  path('doctor/delete/<int:doctor_id>/',views.doctor_delete),
  path('patient/delete/<int:patient_id>/',views.patient_delete),
  path('doctor/edit/<int:doctor_id>/', views.doctor_edit),
  path('patient/edit/<int:patient_id>/', views.patient_edit),
  path('doctors/',views.doctor_organize),
  path('patients/', views.patients_organize),
  path('specialty/',views.specialty_list),
  path('specialty/new/',views.specialty_new),
  path('specialty/delete/<int:specialty_id>/',views.specialty_delete),
  path('specialty/edit/<int:specialty_id>/',views.specialty_edit)
]
