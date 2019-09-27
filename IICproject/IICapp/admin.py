from django.contrib import admin
from IICapp import models
# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.Attendance)
admin.site.register(models.AttendanceStatus)
