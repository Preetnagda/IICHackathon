from django.shortcuts import render,redirect
from django.http import HttpResponse
from IICapp import models,send
from IICapp.send import sendNotificationdef
import os
import datetime
x= datetime.date.today()
# print(x)

# Create your views here.

def login(request):

    request.session.flush()
    if (request.POST):
        # print(request["logid"])
        username = request.POST["logid"]
        password = request.POST["psw"]

        for data in models.Teacher.objects.raw('SELECT * from IICapp_teacher'):
            if(data.username==username):
                if(data.password==password):
                    request.session["username"] = username;
                    return redirect(loggedin)

    return render(request,"login.html")

def loggedin(request):

    if(request.session["username"]):
        teacher = models.Teacher.objects.filter(username = request.session["username"])
        attendedstatus = models.AttendanceStatus.objects.filter(teacher = teacher[0])
        updated = False
        for i in range(len(attendedstatus)):
            print("get attendacne")
            if(attendedstatus[i].date == x):
                updated = True
                loggedincontext = {
                    "updated" : True
                }
                return render(request,"home.html",loggedincontext)
        teacherclass = str(teacher[0].teacher_class)
        teacherstd = str(teacher[0].std)
        loggedincontext = {
            "students" : models.Student.objects.raw('SELECT * from IICapp_student where std = '+teacherstd + ' and stud_class = '+teacherclass),
            "updated" : False,
        }
        return render(request,"home.html",loggedincontext)

    else:
        return redirect(login)

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
        astatus = models.AttendanceStatus(teacher = teacher[0],date=x)
        astatus.save()
    context = {
        "value" : value,
        "teacherclass" : teacherclass,
        "teacherstd" : teacherstd,
    }
    return redirect(loggedin)

def sendNotification(request):
    # teacher = models.Teacher.objects.filter(username = request.session["username"])[0].teacher_class
    teacher = models.Teacher.objects.filter(username = request.session["username"])[0]
    teacherid = teacher.id
    # newsend = new send
    sendNotificationdef(teacherid)
    return redirect(loggedin)
