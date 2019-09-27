from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=50)
    std = models.IntegerField()
    stud_class = models.IntegerField()
    parent_phone_number = models.CharField(max_length=10)
    parent_email_id = models.EmailField()

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    std = models.IntegerField()
    teacher_class = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Attendance(models.Model):
     student = models.ForeignKey(Student, on_delete=models.CASCADE)
     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
     attendace = models.BooleanField()
     date = models.DateField()
