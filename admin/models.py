from django.db import models

class Course(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    fee = models.FloatField()
    duration = models.CharField(max_length=30)

