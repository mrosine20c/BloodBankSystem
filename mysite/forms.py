from django import forms
from django.contrib.auth.models import User
from . import models

class DonorsForm(forms.ModelsForm):
    class Meta:
        model = models.Donors
        fields = ['first_name','last_name','age','body_weight','phone_number','blood_type','blood_quantity','created_by']


class PatientForm(forms.ModelsForm):
    class Meta:
        model = models.Patients
        fields = ['first_name','last_name','age','body_weight','phone_number','blood_type','blood_quantity','hospital']


class HospitalRequest(forms.ModelsForm):
    class Meta:
        model = models.HospitalStock
        field = ['blood_type','blood_quantity','hospital']


