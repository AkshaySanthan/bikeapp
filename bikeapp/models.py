from django.db import models

# Create your models here.


class Bikes(models.Model):
    bike_name=models.CharField(max_length=120)
    registration=models.CharField(max_length=150)
    company_name=models.CharField(max_length=120)
    engine_displacement=models.PositiveIntegerField()
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.bike_name
