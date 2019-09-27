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
        loggedincontext = {
            "students" : models.Student.objects.raw('SELECT * from IICapp_student')
        }
        for data in models.Teacher.objects.raw('SELECT * from IICapp_teacher'):
            if(data.username==username):
                if(data.password==password):
                    request.session["username"] = username;
                    return render(request,"home.html",loggedincontext)

    context = {
    "name":name
    }
    return render(request,"login.html",context)

def updateAttendance(request):
    students =  models.Student.objects.raw('SELECT * from IICapp_student')
    value = ""
    name = "name"
    if(request.POST):
        for student in students:
            status = request.POST["Attendence"+str(student.id)]
            attended = True
            if status == "Present":
                attended = True
            else:
                attended = False

            a = models.Attendance(student=student.id,teacher = models.Teacher.objects.raw('SELECT id from IICapp_teacher where username ='+request.session["username"]),attendace = attended,date=x)
            a.save()
    context = {
    "value" : value,
    }
    return render(request,"newhtml.html",context)
