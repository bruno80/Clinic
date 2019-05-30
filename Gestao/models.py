from django.db import models

class Specialty(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=80)  
    crm = models.CharField(max_length=7, unique=True)
    date_of_birth = models.DateField()
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=80)
    cpf = models.CharField(max_length=11, unique=True)
    date_of_birth = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name