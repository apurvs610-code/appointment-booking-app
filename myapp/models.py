from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone= models.CharField(max_length=11)
    doctor = models.CharField(max_length=11)
    date = models.DateField()
    time = models.TimeField()
    problem = models.CharField(max_length=11)
    def __str__(self):
        return self.name


# Create your models here.
