from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import User
# class collectors(models.Model):


class Donors(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    body_weight = models.IntegerField()
    phone_number = models.CharField(max_length=50) 
    blood_type = models.CharField(max_length =5)
    blood_quantity = models.IntegerField()
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True) 

    class Meta:
        db_table = "donors"


class Patients(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    body_weight = models.IntegerField()
    phone_number = models.CharField(max_length=50) 
    blood_type = models.CharField(max_length =5)
    blood_quantity = models.IntegerField()
    hospital=models.CharField(max_length= 100)

    class Meta:
        db_table = "patients"


class HospitalStock(models.Model):

    blood_type = models.CharField(max_length =5)
    blood_quantity = models.IntegerField()
    hospital=models.ForeignKey(User,on_delete=models.CASCADE) 

    class Meta:
        db_table = "hospital_stock"


class RbcStock(models.Model):
    blood_type = models.CharField(max_length =5)
    blood_quantity = models.IntegerField()

    class Meta:
        db_table = "rbc_stock"


class HospitalRequests(models.Model):
    blood_type = models.CharField(max_length =5)
    blood_quantity = models.IntegerField()
    hospital=models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.IntegerField() 

    class Meta:
        db_table = "hospital_requests"



        
    




