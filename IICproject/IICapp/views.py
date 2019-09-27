from django.shortcuts import render
from django.http import HttpResponse
from IICapp import models
import os

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
