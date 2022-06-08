from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Bikes(models.Model):
    bike_name=models.CharField(max_length=120)
    registration=models.CharField(max_length=150)
    company_name=models.CharField(max_length=120)
    engine_displacement=models.PositiveIntegerField()
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.bike_name



class CompanyProfile(models.Model):
    company_name=models.CharField(max_length=120)
    location=models.CharField(max_length=120)
    services=models.CharField(max_length=120)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="seller")
    logo=models.ImageField(upload_to="companyprofile",null=True)



