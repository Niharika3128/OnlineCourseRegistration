from django.db import models
from admin.models import Course

class StudentInfo(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

class EnrolCourse(models.Model):
    student = models.ForeignKey(StudentInfo,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)