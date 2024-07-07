from django.db import models

class ErrorCharges(models.Model):
    error = models.CharField(max_length=255)
    description = models.TextField()


class Patient(models.Model):
    full_name = models.CharField(max_length=100,null=True,blank=True)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    gender = models.CharField(max_length=100,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    date_of_birth = models.DateField(null=True,blank=True)
    mrn = models.CharField(max_length=500,null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    error_charges = models.ForeignKey('ErrorCharges',on_delete=models.CASCADE,related_name='patient_error_charge',null=True,blank=True)