from django.forms import ModelForm, TextInput, Select, DateInput
from . models import Specialty, Doctor, Patient

class FormDoctor(ModelForm):
    class Meta:
        model = Doctor
        fields = ('__all__')
        widgets = {
            'name': TextInput(attrs={'class':'form-control'}),
            'crm': TextInput(attrs={'class':'form-control'}),
            'date_of_birth': DateInput(attrs={'class':'form-control'}),
            'specialty': Select(attrs={'class':'form-control'})}

class FormPatient(ModelForm):
    class Meta:
        model = Patient
        fields = ('__all__')
        widgets = {
            'name': TextInput(attrs={'class':'form-control'}),
            'cpf': TextInput(attrs={'class':'form-control'}),
            'date_of_birth': DateInput(attrs={'class':'form-control'}),
            'doctor': Select(attrs={'class':'form-control'})}

class FormSpecialty(ModelForm):
    class Meta:
        model = Specialty
        fields = ('__all__')
        widgets = {
            'name': TextInput(attrs={'class':'form-control'}),
            'description': TextInput(attrs={'class':'form-control'})}
            