from django.db import models

# Create your models here.
class PersonalDetails(models.Model):
    Id = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    BirthDay = models.DateField()
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    ZipCode = models.IntegerField()
    LandLine = models.BigIntegerField(max_length=100)
    Phone = models.BigIntegerField()
    isInfected = models.BooleanField()
    isDiabetes = models.BooleanField()
    isCardio = models.BooleanField()
    isAllergic = models.BooleanField()
    otherInput = models.CharField(max_length=100, blank= True)