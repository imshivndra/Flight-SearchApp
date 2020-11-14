from django.db import models

# Create your models here.

class FlightDetails(models.Model):
   number=models.CharField(max_length=20)
   departure_city=models.CharField(max_length=50)
   departure_time=models.BigIntegerField()
   arrival_city=models.CharField(max_length=50)
   arrival_time=models.BigIntegerField()
