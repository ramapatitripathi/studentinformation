from django.db import models

# Create your models here.
class Student(models.Model):
    stname=models.CharField(max_length=100)
    stroll=models.IntegerField(primary_key=True)
    stbranch=models.CharField(max_length=100)
    styear=models.IntegerField()
    staddress=models.CharField(max_length=100)
