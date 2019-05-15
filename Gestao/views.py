from django.shortcuts import render

def home(request):
    return render (request, 'home.html', {})

def doctor_show(request):
    return render(request, 'doctor/show.html',{}) 

def patient_show(request):
    return render(request, 'patient/show.html',{})  