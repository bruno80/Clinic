from django.shortcuts import render, redirect
from . models import Doctor, Specialty, Patient
from django.http import HttpResponse
from . forms import FormDoctor, FormPatient, FormSpecialty
from django.db.models import Count

def home(request):
    visitante = request.session.get('visitante', 0)
    request.session['visitante'] = visitante+1
    return render (request, 'home.html')

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor/list.html',{'doctors':doctors}) 

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient/list.html',{'patients':patients})  

def specialty_list(request):
    specialtys = Specialty.objects.all()
    return render(request, 'specialty/list.html',{'specialtys':specialtys}) 


def doctor_delete(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    doctor.delete()
    return redirect('/gestao/doctor/')

def patient_delete(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    patient.delete()
    return redirect('/gestao/patient/')

def specialty_delete(request, specialty_id):
    specialty = Specialty.objects.get(pk=specialty_id)
    specialty.delete()
    return redirect('/gestao/specialty/')

def doctor_new(request):
    if request.method == 'POST':
        form = FormDoctor(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('/gestao/doctor/')
        else:
            return render(request, 'doctor/form.html', {'form':form})
    else:
        form = FormDoctor()
        return render(request, 'doctor/form.html', {'form':form})

def patient_new(request):
    if request.method == 'POST':
        form = FormPatient(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('/gestao/patient/')
        else:
            return render(request, 'patient/form.html', {'form':form})
    else:
        form = FormPatient()
        return render(request, 'patient/form.html', {'form':form})

def specialty_new(request):
    if request.method == 'POST':
        form = FormSpecialty(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('/gestao/specialty/')
        else:
            return render(request, 'specialty/form.html', {'form':form})
    else:
        form = FormSpecialty()
        return render(request, 'specialty/form.html', {'form':form})

def doctor_edit(request, doctor_id):
    if request.method == 'POST':
        doctor = Doctor.objects.get(pk=doctor_id)
        form = FormDoctor(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('/gestao/doctor/')
        else:
            return render(request, 'doctor/edit.html', {'form':form, 'doctor':doctor})
    else:
        doctor = Doctor.objects.get(pk=doctor_id)
        form = FormDoctor(instance=doctor)
        return render(request, 'doctor/edit.html', {'form':form,'doctor':doctor})

def patient_edit(request, patient_id):
    if request.method == 'POST':
        patient = Patient.objects.get(pk=patient_id)
        form = FormPatient(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('/gestao/patient/')
        else:
            return render(request, 'patient/edit.html', {'form':form, 'patient':patient})
    else:
        patient = Patient.objects.get(pk=patient_id)
        form = FormPatient(instance=patient)
        return render(request, 'patient/edit.html', {'form':form,'patient':patient})

def specialty_edit(request, specialty_id):
    if request.method == 'POST':
        specialty = Specialty.objects.get(pk=specialty_id)
        form = FormSpecialty(request.POST, instance=specialty)
        if form.is_valid():
            form.save()
            return redirect('/gestao/specialty/')
        else:
            return render(request, 'specialty/edit.html', {'form':form, 'specialty':specialty})
    else:
        specialty = Specialty.objects.get(pk=specialty_id)
        form = FormSpecialty(instance=specialty)
        return render(request, 'specialty/edit.html', {'form':form,'specialty':specialty})

def doctor_organize(request):
    if request.method == 'POST':
        form = request.POST.get('select')
        doctors = Doctor.objects.all().order_by(form)
        return render(request, 'doctor/list.html', {'doctors':doctors})
    else:
        doctors = Doctor.objects.all()
        return render(request, 'doctors/list.html', {'doctors':doctors})

def patients_organize(request):
    if request.method == 'POST':
        form = request.POST.get('name')
        patients = Patient.objects.filter(name__icontains=form)
        return render(request, 'patient/list.html', {'patients':patients})
    else:
        patients = Patient.objects.all()
        return render(request, 'patient/list.html', {"patients":patients})