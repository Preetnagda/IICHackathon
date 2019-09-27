from django.shortcuts import render
from django.http import HttpResponse
from IICapp import models
import os
import datetime
x= datetime.datetime.now()

# Create your views here.

def login(request):
    name = ""
    if (request.POST):
        # print(request["logid"])
        username = request.POST["logid"]
        password = request.POST["psw"]

        for data in models.Teacher.objects.raw('SELECT * from IICapp_teacher'):
            if(data.username==username):
                if(data.password==password):
                    request.session["username"] = username;
                    teacherclass = str(models.Teacher.objects.filter(username = request.session["username"])[0].teacher_class)
                    teacherstd = str(models.Teacher.objects.filter(username = request.session["username"])[0].std)
                    loggedincontext = {
                        "students" : models.Student.objects.raw('SELECT * from IICapp_student where std = '+teacherstd + ' and stud_class = '+teacherclass)
                    }
                    return render(request,"home.html",loggedincontext)

    context = {
    "name":name
    }
    return render(request,"login.html",context)

def updateAttendance(request):
    teacherclass = str(models.Teacher.objects.filter(username = request.session["username"])[0].teacher_class)
    teacherstd = str(models.Teacher.objects.filter(username = request.session["username"])[0].std)
    students =  models.Student.objects.raw('SELECT * from IICapp_student where std = '+teacherstd + ' and stud_class = '+teacherclass)
    value = teacherclass
    name = "name"
    if(request.POST):
        for student in students:
            status = request.POST["Attendence"+str(student.id)]
            attended = True
            # teacherid =  str(models.Teacher.objects.raw('SELECT id from IICapp_teacher where username ='+request.session["username"]))
            teacher = models.Teacher.objects.filter(username = request.session["username"])
            if status == "Present":
                attended = True
            else:
                attended = False
            a = models.Attendance(student=student,teacher = teacher[0] ,attendace = attended,date=x)
            a.save()
    context = {
        "value" : value,
        "teacherclass" : teacherclass,
        "teacherstd" : teacherstd,
    }
    return render(request,"newhtml.html",context)
